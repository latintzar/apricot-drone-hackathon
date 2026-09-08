import copy
import json
import tempfile
import unittest
from pathlib import Path
from replay import load_records, render, ROOT

class ReplayTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / 'sample/trees.json').read_text())

    def load(self, data):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'data.json'
            path.write_text(json.dumps(data))
            return load_records(path)

    def test_duplicate_ids_rejected(self):
        self.data['trees'][1]['id'] = self.data['trees'][0]['id']
        with self.assertRaises(ValueError): self.load(self.data)

    def test_invalid_positions_rejected(self):
        for value in [-1, 101, float('nan'), float('inf'), True]:
            with self.subTest(value=value):
                data = copy.deepcopy(self.data)
                data['trees'][0]['x'] = value
                with self.assertRaises(ValueError): self.load(data)

    def test_text_cannot_close_data_script(self):
        attack = '</script><script>alert(1)</script>'
        self.data['trees'][0]['observation'] = attack
        page = render(self.load(self.data))
        self.assertNotIn(attack, page)
        payload = page.split('type="application/json">')[1].split('</script>')[0]
        self.assertEqual(json.loads(payload)['trees'][0]['observation'], attack)

if __name__ == '__main__': unittest.main()

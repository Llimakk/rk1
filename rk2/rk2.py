import unittest
from rk1 import *
class test_prog(unittest.TestCase):
    manufacturers = [
        Manufacturer(1, 'Дом в уюте'),
        Manufacturer(2, 'Строй в удовольствие'),
        Manufacturer(3, 'Домашний помощник'),
        Manufacturer(4, 'Леруа мерлен'),
    ]

    details = [
        Detail(1, 'Подшипник', 600, 1),
        Detail(2, 'Колесо', 800, 1),
        Detail(3, 'Винт', 400, 2),
        Detail(4, 'Болт', 450, 3),
        Detail(5, 'Втулка', 700, 3),
    ]

    det_man = [
        DetMan(1, 1),
        DetMan(1, 4),
        DetMan(2, 3),
        DetMan(3, 2),
        DetMan(3, 3),
        DetMan(3, 4),
        DetMan(4, 1),
        DetMan(4, 3),
        DetMan(5, 3),
        DetMan(5, 2),
    ]


    def test_g1(self):
        o_to_m = [(d.name, d.price, m.title) for d in details for m in manufacturers if d.man_id == m.id]
        self.assertEqual(g1(o_to_m), {'Дом в уюте': [('Подшипник', 606), ('Колесо', 800)], 'Домашний помощник': [('Болт', 450), ('Втулка', 700)]})


    def test_g2(self):
        o_to_m = [(d.name, d.price, m.title) for d in details for m in manufacturers if d.man_id == m.id]
        self.assertEqual(g2(o_to_m), [('Дом в уюте', 800), ('Дом в уюте', 800), ('Домашний помощник', 700), ('Домашний помощник', 700)])

    def test_g3(self):
        m_to_m = [(m.title, dm.man_id, dm.det_id) for m in manufacturers for dm in det_man if m.id == dm.man_id]
        m_to_m = [(d.name , d.price , man_title) for man_title, man_id, det_id in m_to_m for d in details if d.id == det_id]
        self.assertEqual(g3(m_to_m), [('Подшипник', 600, 'Дом в уюте'), ('Болт', 450, 'Дом в уюте'), ('Колесо', 800, 'Домашний помощник'), ('Винт', 400, 'Домашний помощник'), ('Болт', 450, 'Домашний помощник'), ('Подшипник', 600, 'Леруа мерлен'), ('Винт', 400, 'Леруа мерлен'), ('Винт', 400, 'Строй в удовольствие')])

if __name__ == '__main__':
    main()

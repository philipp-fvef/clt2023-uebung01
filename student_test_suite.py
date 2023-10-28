# -*-coding:utf-8 -*-
# Date: 2022-10-24 13:45:07

import rd


class TestRecursiveDecent():

    def test_pass(self):
        assert rd.parse_S(["Hans", "isst", "ein", "Kaesebrot"], 0, 4) == True

    def test_NP(self):
        assert rd.parse_NP(["Hans", "isst", "ein", "Kaesebrot"], 2, 4) == True

    def test_N(self):
        assert rd.parse_N(["Hans", "isst", "ein", "Kaesebrot"], 0, 1) == False

    def test_VP(self):
        assert rd.parse_VP(["Hans", "isst", "ein", "Kaesebrot"], 1, 4) == True

    def test_V(self):
        assert rd.parse_V(["Hans", "isst", "ein", "Kaesebrot"], 0, 1) == False

#!/usr/bin/env python3

"""
tests.py -- Unit Tests
"""

import unittest

import gis


# Testing data
decimal_data = (
    (-71.93673621809617, -137.26408647331579),
    (-80.33269149472957, -70.7004193013188),
    (-63.10771626353747, -9.30844763944247),
    (-88.16608069915864, 11.011619809343289),
    (-64.7859412813925, 116.03044420282737),
    (-62.28512282940016, 126.22519158271169),
    (-32.03944204062819, -139.8818491137525),
    (-36.8937227123101, -68.88941904236744),
    (-32.2899831508026, -10.18770716915023),
    (-42.37502888208036, 58.22533405419908),
    (-55.083148970566754, 102.43783559872301),
    (-38.70930412658066, 170.0389591468604),
    (-27.259119141478262, -175.57639961875287),
    (-23.234562722553555, -83.86380367426824),
    (-29.017271315049243, -13.05238288416411),
    (-16.751015012802533, 58.945251028857875),
    (-18.350878260572287, 67.01671685632066),
    (-22.263861359883503, 147.03567400889045),
    (21.86458692175361, -176.96246361422703),
    (9.943815247525169, -95.63061724498469),
    (22.443321953437316, -44.39690679705765),
    (28.681767288229622, 33.951196539513305),
    (16.786394830922408, 75.34131893507416),
    (21.222556239365005, 153.02297497916038),
    (32.84883124506498, -138.86919214065847),
    (35.01497321120664, -103.06892682417492),
    (41.92158437272542, -52.64021054689153),
    (48.372302838305544, 17.789663143061038),
    (59.99172139999361, 73.30923989653196),
    (45.478856236456764, 146.07879882900477),
    (80.5635787869228, -150.21913438668616),
    (64.47004709624093, -67.29523381230405),
    (60.86918907911827, -14.72613548486116),
    (87.46842851812718, 43.16847461918086),
    (85.54276629368051, 65.58432801288734),
    (60.46861296069463, 179.41271000437132)
)

utm_data = (
    (421662, 2016652.3, 8, -1),
    (468126.4, 1080814.1, 19, -1),
    (484434, 3002371.9, 29, -1),
    (507186.1, 206664.1, 32, -1),
    (453914.8, 2815048.7, 50, -1),
    (356055, 3090969.7, 52, -1),
    (605573, 6454645.9, 7, -1),
    (509852.7, 5916911.5, 19, -1),
    (388165.8, 6426801.9, 29, -1),
    (600881.9, 5307856.3, 40, -1),
    (336460, 3892956.6, 48, -1),
    (416441.5, 5715043.2, 59, -1),
    (640926.1, 6984062.4, 1, -1),
    (206938, 7427622.9, 17, -1),
    (689685.7, 6788536.6, 28, -1),
    (707363.7, 8146973.8, 40, -1),
    (290429.8, 7969851.7, 42, -1),
    (503675.5, 7537966.4, 55, -1),
    (503878.2, 2417839.2, 1, 1),
    (211550.8, 1100344.6, 15, 1),
    (562057.3, 2482022.5, 23, 1),
    (592931.1, 3173099.2, 36, 1),
    (536372.2, 1855956.5, 43, 1),
    (502384.2, 2346779, 56, 1),
    (699409, 3636540.4, 7, 1),
    (676193, 3876407.6, 13, 1),
    (363993, 4642370.7, 22, 1),
    (706585.2, 5361442.1, 33, 1),
    (405676.6, 6651694.5, 43, 1),
    (428002.6, 5036560.2, 55, 1),
    (550880.9, 8945709.2, 5, 1),
    (581972.6, 7150495, 19, 1),
    (514873, 6748248.2, 28, 1),
    (490969.4, 9715462.8, 38, 1),
    (522415.8, 9500832.1, 41, 1),
    (632647.5, 6706032, 60, 1)
)


class GeodesyTest(unittest.TestCase):
    """ Test geodetic point data conversion. """

    def test_from_utm(self):
        for (_latitude, _longitude), utm in zip(decimal_data, utm_data):
            latitude, longitude = gis.geodesy.from_utm(*utm)
            self.assertAlmostEqual(latitude, _latitude, 4)
            self.assertAlmostEqual(longitude, _longitude, 4)

    def test_to_utm(self):
        for decimals, utm_ in zip(decimal_data, utm_data):
            utm = gis.geodesy.to_utm(*decimals)
            for a, b in zip(utm, utm_):
                self.assertAlmostEqual(a, b)
                #self.assertAlmostEqual(a, b, -5)


if __name__ == '__main__':
    unittest.main()

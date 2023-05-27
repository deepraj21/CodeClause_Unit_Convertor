import streamlit as st
import requests
conversion_factors_length = {
    'meter': {
        'meter': 1,
        'kilometer': 0.001,
        'mile': 0.000621371,
        'decimeter': 10.0,
        'centimeter': 100.0,
        'millimeter': 1000.0,
        'micrometer': 1000000.0,
        'nanometer': 1000000000.0,
        'picometer': 1000000000000.0,
        'furlog': 0.000497096,
        'fathom': 0.546807,
        'yard': 1.09361,
        'foot': 3.28084,
        'inch': 39.3701,
        'astronomical_unit': 6.68459e-12,
        'light_year': 1.057e-16
    },
    'kilometer': {
        'kilometer':1,
        'meter': 1000.0,
        'mile': 0.621371,
        'decimeter': 10000.0,
        'centimeter': 100000.0,
        'millimeter': 1000000.0,
        'micrometer': 1000000000.0,
        'nanometer': 1000000000000.0,
        'picometer': 1000000000000000.0,
        'furlog': 4.97096,
        'fathom': 546.807,
        'yard': 1093.61,
        'foot': 3280.84,
        'inch': 39370.1,
        'astronomical_unit': 6.68459e-9,
        'light_year': 1.057e-13
    },
    'mile': {
        'mile' :1,
        'meter': 1609.34,
        'kilometer': 1.60934,
        'decimeter': 16093.4,
        'centimeter': 160934.0,
        'millimeter': 1609340.0,
        'micrometer': 1609340000.0,
        'nanometer': 1609340000000.0,
        'picometer': 1609340000000000.0,
        'furlog': 8.01505,
        'fathom': 880.0,
        'yard': 1760.0,
        'foot': 5280.0,
        'inch': 63360.0,
        'astronomical_unit': 3.40539e-8,
        'light_year': 5.368e-13
    },
    'decimeter': {
        'decimeter':1,
        'meter': 0.1,
        'kilometer': 0.0001,
        'mile': 0.0000621371,
        'centimeter': 10.0,
        'millimeter': 100.0,
        'micrometer': 100000.0,
        'nanometer': 100000000.0,
        'picometer': 100000000000.0,
        'furlog': 0.0000497096,
        'fathom': 0.0546807,
        'yard': 0.109361,
        'foot': 0.328084,
        'inch': 3.93701,
        'astronomical_unit': 6.68459e-14,
        'light_year': 1.057e-18
    },
    'centimeter': {
        'centimeter':1,
        'meter': 0.01,
        'kilometer': 0.00001,
        'mile': 0.00000621371,
        'decimeter': 0.1,
        'millimeter': 10.0,
        'micrometer': 10000.0,
        'nanometer': 10000000.0,
        'picometer': 10000000000.0,
        'furlog': 0.00000497096,
        'fathom': 0.00546807,
        'yard': 0.0109361,
        'foot': 0.0328084,
        'inch': 0.393701,
        'astronomical_unit': 6.68459e-16,
        'light_year': 1.057e-20
    },
    'millimeter': {
        'millimeter':1,
        'meter': 0.001,
        'kilometer': 0.000001,
        'mile': 6.2137e-7,
        'decimeter': 0.01,
        'centimeter': 0.1,
        'micrometer': 1000.0,
        'nanometer': 1000000.0,
        'picometer': 1000000000.0,
        'furlog': 4.97096e-7,
        'fathom': 0.000546807,
        'yard': 0.00109361,
        'foot': 0.00328084,
        'inch': 0.0393701,
        'astronomical_unit': 6.68459e-19,
        'light_year': 1.057e-23
    },
    'micrometer': {
        'micrometer':1,
        'meter': 0.000001,
        'kilometer': 1e-9,
        'mile': 6.2137e-10,
        'decimeter': 0.00001,
        'centimeter': 0.0001,
        'millimeter': 0.001,
        'nanometer': 1000.0,
        'picometer': 1000000.0,
        'furlog': 4.97096e-10,
        'fathom': 5.46807e-7,
        'yard': 0.00000109361,
        'foot': 0.00000328084,
        'inch': 0.0000393701,
        'astronomical_unit': 6.68459e-22,
        'light_year': 1.057e-26
    },
    'nanometer': {
        'nanometer':1,
        'meter': 1e-9,
        'kilometer': 1e-12,
        'mile': 6.2137e-13,
        'decimeter': 1e-8,
        'centimeter': 1e-7,
        'millimeter': 0.000001,
        'micrometer': 0.001,
        'picometer': 1000.0,
        'furlog': 4.97096e-13,
        'fathom': 5.46807e-10,
        'yard': 1.09361e-9,
        'foot': 3.28084e-9,
        'inch': 3.93701e-8,
        'astronomical_unit': 6.68459e-25,
        'light_year': 1.057e-29
    },
    'picometer': {
        'picometer':1,
        'meter': 1e-12,
        'kilometer': 1e-15,
        'mile': 6.2137e-16,
        'decimeter': 1e-11,
        'centimeter': 1e-10,
        'millimeter': 1e-9,
        'micrometer': 0.001,
        'nanometer': 0.001,
        'furlog': 4.97096e-16,
        'fathom': 5.46807e-13,
        'yard': 1.09361e-12,
        'foot': 3.28084e-12,
        'inch': 3.93701e-11,
        'astronomical_unit': 6.68459e-31,
        'light_year': 1.057e-35
    },
    'furlog': {
        'furlog':1,
        'meter': 2011.68,
        'kilometer': 2.01168,
        'mile': 1.25,
        'decimeter': 20116.8,
        'centimeter': 201168.0,
        'millimeter': 2011680.0,
        'micrometer': 2011680000.0,
        'nanometer': 2011680000000.0,
        'picometer': 2011680000000000.0,
        'fathom': 1093.61,
        'yard': 2187.22,
        'foot': 6561.68,
        'inch': 78740.2,
        'astronomical_unit': 1.33782e-8,
        'light_year': 2.111e-13
    },
    'fathom': {
        'fathom':1,
        'meter': 1.8288,
        'kilometer': 0.0018288,
        'mile': 0.00113636,
        'decimeter': 18.288,
        'centimeter': 182.88,
        'millimeter': 1828.8,
        'micrometer': 1828800.0,
        'nanometer': 1828800000.0,
        'picometer': 1828800000000.0,
        'furlog': 0.000893939,
        'yard': 2.0,
        'foot': 6.0,
        'inch': 72.0,
        'astronomical_unit': 4.84814e-10,
        'light_year': 7.639e-15
    },
    'yard': {
        'yard':1,
        'meter': 0.9144,
        'kilometer': 0.0009144,
        'mile': 0.000568182,
        'decimeter': 9.144,
        'centimeter': 91.44,
        'millimeter': 914.4,
        'micrometer': 914400.0,
        'nanometer': 914400000.0,
        'picometer': 914400000000.0,
        'furlog': 0.000454545,
        'fathom': 0.546807,
        'foot': 3.0,
        'inch': 36.0,
        'astronomical_unit': 2.44794e-9,
        'light_year': 3.8785e-14
    },
    'foot': {
        'foot':1,
        'meter': 0.3048,
        'kilometer': 0.0003048,
        'mile': 0.000189394,
        'decimeter': 3.048,
        'centimeter': 30.48,
        'millimeter': 304.8,
        'micrometer': 304800.0,
        'nanometer': 304800000.0,
        'picometer': 304800000000.0,
        'furlog': 0.000151515,
        'fathom': 0.18288,
        'yard': 0.333333,
        'inch': 12.0,
        'astronomical_unit': 8.23157e-10,
        'light_year': 1.3008e-14
    },
    'inch': {
        'inch':1,
        'meter': 0.0254,
        'kilometer': 2.54e-5,
        'mile': 1.5783e-5,
        'decimeter': 0.254,
        'centimeter': 2.54,
        'millimeter': 25.4,
        'micrometer': 25400.0,
        'nanometer': 25400000.0,
        'picometer': 25400000000.0,
        'furlog': 1.26263e-5,
        'fathom': 0.0157828,
        'yard': 0.0277778,
        'foot': 0.0833333,
        'astronomical_unit': 2.16421e-11,
        'light_year': 3.434e-16
    },
    'astronomical_unit': {
        'astronomical_unit':1,
        'meter': 149597870700.0,
        'kilometer': 149597870.7,
        'mile': 92955807.3,
        'decimeter': 1495978707000.0,
        'centimeter': 14959787070000.0,
        'millimeter': 149597870700000.0,
        'micrometer': 149597870700000000.0,
        'nanometer': 149597870700000000000.0,
        'picometer': 149597870700000000000000.0,
        'furlog': 745650.537,
        'fathom': 8182204344.26,
        'yard': 163644086885.0,
        'foot': 490932260656.0,
        'inch': 5891187127870.0,
        'light_year': 0.000158692
    },
    'light_year': {
        'light_year':1,
        'meter': 9460730472580800.0,
        'kilometer': 9460730472580.8,
        'mile': 5878625373183.66,
        'decimeter': 94607304725808000.0,
        'centimeter': 946073047258080000.0,
        'millimeter': 9460730472580800000.0,
        'micrometer': 9460730472580800000000.0,
        'nanometer': 9460730472580800000000000.0,
        'picometer': 9460730472580800000000000000.0,
        'furlog': 4712742182075.68,
        'fathom': 51837960111798000.0,
        'yard': 1036759202235960000.0,
        'foot': 3110277606707880000.0,
        'inch': 37323331280494600000.0,
        'astronomical_unit': 6.30957e+12
    }
}

conversion_factors_mass = {
        'kilogram': {
            'kilogram':1.0,
            'gram': 1000.0,
            'milligram': 1000000.0,
            'microgram': 1000000000.0,
            'quintal': 0.01,
            'pound': 2.20462,
            'ounce': 35.274,
            'carat': 5000.0,
            'grain': 15432.4,
        },
        'gram': {
            'gram':1,
            'kilogram': 0.001,
            'milligram': 1000.0,
            'microgram': 1000000.0,
            'quintal': 0.00001,
            'pound': 0.00220462,
            'ounce': 0.035274,
            'carat': 5.0,
            'grain': 15.4324,
        },
        'milligram': {
            'milligram':1,
            'kilogram': 1e-6,
            'gram': 0.001,
            'microgram': 1000.0,
            'quintal': 1e-8,
            'pound': 2.20462e-6,
            'ounce': 3.5274e-5,
            'carat': 0.005,
            'grain': 0.0154324,
        },
        'microgram': {
            'microgram':1,
            'kilogram': 1e-9,
            'gram': 1e-6,
            'milligram': 0.001,
            'quintal': 1e-11,
            'pound': 2.20462e-9,
            'ounce': 3.5274e-8,
            'carat': 5e-7,
            'grain': 1.54324e-6,
        },
        'quintal': {
            'quintal':1,
            'kilogram': 100.0,
            'gram': 100000.0,
            'milligram': 100000000.0,
            'microgram': 100000000000.0,
            'pound': 220.462,
            'ounce': 3527.4,
            'carat': 500000.0,
            'grain': 154324.0,
        },
        'pound': {
            'pound':1,
            'kilogram': 0.453592,
            'gram': 453.592,
            'milligram': 453592.0,
            'microgram': 453592000.0,
            'quintal': 0.00453592,
            'ounce': 16.0,
            'carat': 2267.96,
            'grain': 7000.0,
        },
        'ounce': {
            'ounce':1,
            'kilogram': 0.0283495,
            'gram': 28.3495,
            'milligram': 28349.5,
            'microgram': 28349500.0,
            'quintal': 0.000283495,
            'pound': 0.0625,
            'carat': 141.747,
            'grain': 437.5,
        },
        'carat': {
            'carat':1,
            'kilogram': 0.0002,
            'gram': 0.2,
            'milligram': 200.0,
            'microgram': 200000.0,
            'quintal': 2e-6,
            'pound': 0.000440925,
            'ounce': 0.00705479,
            'grain': 3.08647,
        },
        'grain': {
            'grain':1,
            'kilogram': 0.00006479891,
            'gram': 0.06479891,
            'milligram': 64.79891,
            'microgram': 64798.91,
            'quintal': 6.479891e-7,
            'pound': 0.000142857,
            'ounce': 0.00228571,
            'carat': 0.324,
        },   
}

conversion_factors_temp = {
        'celsius': {
            'celsius': lambda x: x,
            'fahrenheit': lambda x: (x * 9/5) + 32,
            'kelvin': lambda x: x + 273.15,
            'rankine': lambda x: (x + 273.15) * 9/5
        },
        'fahrenheit': {
            'celsius': lambda x: (x - 32) * 5/9,
            'fahrenheit': lambda x: x,
            'kelvin': lambda x: (x + 459.67) * 5/9,
            'rankine': lambda x: x + 459.67
        },
        'kelvin': {
            'celsius': lambda x: x - 273.15,
            'fahrenheit': lambda x: (x * 9/5) - 459.67,
            'kelvin': lambda x: x,
            'rankine': lambda x: x * 9/5
        },
        'rankine': {
            'celsius': lambda x: (x - 491.67) * 5/9,
            'fahrenheit': lambda x: x - 459.67,
            'kelvin': lambda x: x * 5/9,
            'rankine': lambda x: x
        }
}

conversion_factors_time = {
        'year': {
            'year': 1,
            'week': 52.143,
            'day': 365,
            'hour': 8760,
            'minute': 525600,
            'second': 31536000,
            'millisecond': 31536000000
        },
        'week': {
            'year': 0.01917,
            'week': 1,
            'day': 7,
            'hour': 168,
            'minute': 10080,
            'second': 604800,
            'millisecond': 604800000
        },
        'day': {
            'year': 0.00274,
            'week': 0.14286,
            'day': 1,
            'hour': 24,
            'minute': 1440,
            'second': 86400,
            'millisecond': 86400000
        },
        'hour': {
            'year': 0.000114155,
            'week': 0.00595238,
            'day': 0.04167,
            'hour': 1,
            'minute': 60,
            'second': 3600,
            'millisecond': 3600000
        },
        'minute': {
            'year': 0.0000019026,
            'week': 0.000099206,
            'day': 0.00069444,
            'hour': 0.016667,
            'minute': 1,
            'second': 60,
            'millisecond': 60000
        },
        'second': {
            'year': 3.1709791983765e-8,
            'week': 1.6534391534392e-6,
            'day': 1.1574074074074e-5,
            'hour': 0.0002777778,
            'minute': 0.0166666667,
            'second': 1,
            'millisecond': 1000
        },
        'millisecond': {
            'year': 3.1709791983765e-11,
            'week': 1.6534391534392e-9,
            'day': 1.1574074074074e-8,
            'hour': 2.7777777777778e-7,
            'minute': 1.6666666666667e-5,
            'second': 0.001,
            'millisecond': 1
        }
}

conversion_factors_speed = {
        'lightspeed': {
            'lightspeed': 1,
            'meter_per_second': 299792458,
            'kilometer_per_hour': 1079252848.8,
            'kilometer_per_second': 299792.458,
            'knot': 582749912,
            'mile_per_hour': 670616629,
            'foot_per_second': 983571057
        },
        'meter_per_second': {
            'lightspeed': 3.3356409519815e-9,
            'meter_per_second': 1,
            'kilometer_per_hour': 3.6,
            'kilometer_per_second': 0.001,
            'knot': 1.9438444924406,
            'mile_per_hour': 2.2369362920544,
            'foot_per_second': 3.2808398950131
        },
        'kilometer_per_hour': {
            'lightspeed': 9.2656693110598e-10,
            'meter_per_second': 0.27777777777778,
            'kilometer_per_hour': 1,
            'kilometer_per_second': 0.00027777777777778,
            'knot': 0.53995680345572,
            'mile_per_hour': 0.62137119223733,
            'foot_per_second': 0.91134441528141
        },
        'kilometer_per_second': {
            'lightspeed': 3.3356409519815e-6,
            'meter_per_second': 1000,
            'kilometer_per_hour': 3600,
            'kilometer_per_second': 1,
            'knot': 1943.8444924406,
            'mile_per_hour': 2236.9362920544,
            'foot_per_second': 3280.8398950131
        },
        'knot': {
            'lightspeed': 1.7160019191533e-9,
            'meter_per_second': 0.51444444444444,
            'kilometer_per_hour': 1.852,
            'kilometer_per_second': 0.00051444444444444,
            'knot': 1,
            'mile_per_hour': 1.1507794480235,
            'foot_per_second': 1.6878098571012
        },
        'mile_per_hour': {
            'lightspeed': 1.4911640202791e-9,
            'meter_per_second': 0.44704,
            'kilometer_per_hour': 1.609344,
            'kilometer_per_second': 0.00044704,
            'knot': 0.86897624190065,
            'mile_per_hour': 1,
            'foot_per_second': 1.4666666666667
        },
        'foot_per_second': {
            'lightspeed': 1.0792528488e-9,
            'meter_per_second': 0.3048,
            'kilometer_per_hour': 1.09728,
            'kilometer_per_second': 0.0003048,
            'knot': 0.5924838012959,
            'mile_per_hour': 0.68181818181818,
            'foot_per_second': 1
        }
}

conversion_factors_volume = {
        'cubic_meter': {
            'cubic_meter': 1,
            'cubic_decimeter': 1000,
            'cubic_centimeter': 1000000,
            'cubic_millimeter': 1000000000,
            'hectoliter': 10,
            'liter': 1000,
            'deciliter': 10000,
            'centiliter': 100000,
            'cubic_foot': 35.3147,
            'cubic_inch': 61023.7,
            'acre_foot': 0.000810714
        },
        'cubic_decimeter': {
            'cubic_meter': 0.001,
            'cubic_decimeter': 1,
            'cubic_centimeter': 1000,
            'cubic_millimeter': 1000000,
            'hectoliter': 0.01,
            'liter': 1,
            'deciliter': 10,
            'centiliter': 100,
            'cubic_foot': 0.0353147,
            'cubic_inch': 61.0237,
            'acre_foot': 8.10714e-8
        },
        'cubic_centimeter': {
            'cubic_meter': 1e-6,
            'cubic_decimeter': 0.001,
            'cubic_centimeter': 1,
            'cubic_millimeter': 1000,
            'hectoliter': 1e-5,
            'liter': 0.001,
            'deciliter': 0.01,
            'centiliter': 0.1,
            'cubic_foot': 3.53147e-5,
            'cubic_inch': 0.0610237,
            'acre_foot': 8.10714e-11
        },
        'cubic_millimeter': {
            'cubic_meter': 1e-9,
            'cubic_decimeter': 1e-6,
            'cubic_centimeter': 0.001,
            'cubic_millimeter': 1,
            'hectoliter': 1e-8,
            'liter': 1e-6,
            'deciliter': 1e-5,
            'centiliter': 0.0001,
            'cubic_foot': 3.53147e-8,
            'cubic_inch': 0.0000610237,
            'acre_foot': 8.10714e-14
        },
        'hectoliter': {
            'cubic_meter': 0.1,
            'cubic_decimeter': 100,
            'cubic_centimeter': 100000,
            'cubic_millimeter': 100000000,
            'hectoliter': 1,
            'liter': 100,
            'deciliter': 1000,
            'centiliter': 10000,
            'cubic_foot': 3.53147,
            'cubic_inch': 61023.7,
            'acre_foot': 0.000810714
        },
        'liter': {
            'cubic_meter': 0.001,
            'cubic_decimeter': 1,
            'cubic_centimeter': 1000,
            'cubic_millimeter': 1000000,
            'hectoliter': 0.01,
            'liter': 1,
            'deciliter': 10,
            'centiliter': 100,
            'cubic_foot': 0.0353147,
            'cubic_inch': 61.0237,
            'acre_foot': 8.10714e-8
        },
        'deciliter': {
            'cubic_meter': 0.0001,
            'cubic_decimeter': 0.1,
            'cubic_centimeter': 100,
            'cubic_millimeter': 100000,
            'hectoliter': 0.001,
            'liter': 0.1,
            'deciliter': 1,
            'centiliter': 10,
            'cubic_foot': 0.00353147,
            'cubic_inch': 6.10237,
            'acre_foot': 8.10714e-9
        },
        'centiliter': {
            'cubic_meter': 1e-5,
            'cubic_decimeter': 0.01,
            'cubic_centimeter': 10,
            'cubic_millimeter': 10000,
            'hectoliter': 1e-4,
            'liter': 0.01,
            'deciliter': 0.1,
            'centiliter': 1,
            'cubic_foot': 0.000353147,
            'cubic_inch': 0.610237,
            'acre_foot': 8.10714e-10
        },
        'cubic_foot': {
            'cubic_meter': 0.0283168,
            'cubic_decimeter': 28.3168,
            'cubic_centimeter': 28316.8,
            'cubic_millimeter': 28316846.6,
            'hectoliter': 0.283168,
            'liter': 28.3168,
            'deciliter': 283.168,
            'centiliter': 2831.68,
            'cubic_foot': 1,
            'cubic_inch': 1728,
            'acre_foot': 0.0000229568
        },
        'cubic_inch': {
            'cubic_meter': 0.0000163871,
            'cubic_decimeter': 0.0163871,
            'cubic_centimeter': 16.3871,
            'cubic_millimeter': 16387.1,
            'hectoliter': 0.000163871,
            'liter': 0.0163871,
            'deciliter': 0.163871,
            'centiliter': 1.63871,
            'cubic_foot': 0.000578704,
            'cubic_inch': 1,
            'acre_foot': 1.35256e-8
        },
        'acre_foot': {
            'cubic_meter': 1233.48,
            'cubic_decimeter': 1.23348e+6,
            'cubic_centimeter': 1.23348e+9,
            'cubic_millimeter': 1.23348e+12,
            'hectoliter': 1.23348e+4,
            'liter': 1.23348e+6,
            'deciliter': 1.23348e+7,
            'centiliter': 1.23348e+8,
            'cubic_foot': 43559.9,
            'cubic_inch': 7.48052e+7,
            'acre_foot': 1
        }
}

def convert_volume(value, from_unit, to_unit):
    if from_unit not in conversion_factors_volume or to_unit not in conversion_factors_volume:
        return None

    result = value * conversion_factors_volume[from_unit][to_unit]
    return result

def convert_speed(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    conversion_factor = conversion_factors_speed[from_unit][to_unit]
    result = value * conversion_factor
    return result
 

def convert_time(value, from_unit, to_unit):

    if from_unit == to_unit:
        return value

    conversion_factor = conversion_factors_time[from_unit][to_unit]
    result = value * conversion_factor
    return result

def convert_units_length(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    if from_unit not in conversion_factors_length or to_unit not in conversion_factors_length[from_unit]:
        return None  # Invalid conversion units

    value = value * conversion_factors_length[from_unit][to_unit]
    result = value / conversion_factors_length[to_unit][to_unit]
    return result

def convert_units_mass(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    if from_unit not in conversion_factors_mass or to_unit not in conversion_factors_mass[from_unit]:
        return None  # Invalid conversion units

    value = value * conversion_factors_mass[from_unit][to_unit]
    result = value / conversion_factors_mass[to_unit][to_unit]
    return result

def convert_temperature(value, from_unit, to_unit):
    
    if from_unit == to_unit:
        return value

    convert_func = conversion_factors_temp[from_unit][to_unit]
    result = convert_func(value)
    return result

def main():
    
    st.set_page_config(page_title="Unitify",page_icon='https://cdn4.iconfinder.com/data/icons/business-1219/24/Calculator-256.png' ,layout="wide")
    st.title('Universal Unitify')
    st.subheader('"Unlock the Power of Conversion: Your All-in-One Unit Conversion Solution"')
    st.markdown("<hr>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.title(" 📏 Length Conversion")
        from_unit_length = st.selectbox("From Unit", list(conversion_factors_length.keys()))
        to_unit_length = st.selectbox("To Unit", list(conversion_factors_length.keys()))

        value_length = st.number_input("Enter Value",key="value_length")

        converted_value_length = convert_units_length(value_length, from_unit_length, to_unit_length)
        
        if converted_value_length is None:
            st.error("Invalid conversion units")
        else:
            result_length = f"{value_length} {from_unit_length} = {converted_value_length} {to_unit_length}"
            st.markdown(f"<p style='text-align: center;'>{result_length}</p>", unsafe_allow_html=True)
    
    with col2:
        st.title(" ⚖️  Mass Conversion")
        from_unit_mass = st.selectbox("From Unit", list(conversion_factors_mass.keys()))
        to_unit_mass = st.selectbox("To Unit", list(conversion_factors_mass.keys()))

        value_mass = st.number_input("Enter Value",key="value_mass")

        converted_value_mass = convert_units_mass(value_mass, from_unit_mass, to_unit_mass)

        if converted_value_mass is None:
            st.error("Invalid conversion units")
        else:
            result_mass = f"{value_mass} {from_unit_mass} = {converted_value_mass} {to_unit_mass}"
            st.markdown(f"<p style='text-align: center;'>{result_mass}</p>", unsafe_allow_html=True)

    col3,col4= st.columns(2)
    with col3:
        st.title(" 🌡️ Temp Conversion")
        from_unit_temp = st.selectbox("From Unit", list(conversion_factors_temp.keys()))
        to_unit_temp = st.selectbox("To Unit", list(conversion_factors_temp.keys()))

        value_temp = st.number_input("Enter Value",key="value_temp")

        converted_value_temp = convert_temperature(value_temp, from_unit_temp, to_unit_temp)

        if converted_value_mass is None:
            st.error("Invalid conversion units")
        else:
            result_temp = f"{value_temp} {from_unit_temp} = {converted_value_temp} {to_unit_temp}"
            st.markdown(f"<p style='text-align: center;'>{result_temp}</p>", unsafe_allow_html=True)
    
    with col4:
        st.title(" 🕑 Time Conversion")
        from_unit_time = st.selectbox("From Unit", list(conversion_factors_time.keys()))
        to_unit_time = st.selectbox("To Unit", list(conversion_factors_time.keys()))

        value_time = st.number_input("Enter Value",key="value_time")

        converted_value_time = convert_time(value_time, from_unit_time, to_unit_time)

        if converted_value_time is None:
            st.error("Invalid conversion units")
        else:
            result_time = f"{value_time} {from_unit_time} = {converted_value_time} {to_unit_time}"
            st.markdown(f"<p style='text-align: center;'>{result_time}</p>", unsafe_allow_html=True)
    
    col5,col6=st.columns(2)
    with col5:
        st.title(" ⏱️ Speed Conversion")
        from_unit_speed = st.selectbox("From Unit", list(conversion_factors_speed.keys()))
        to_unit_speed = st.selectbox("To Unit", list(conversion_factors_speed.keys()))

        value_speed = st.number_input("Enter Value",key="value_speed")

        converted_value_speed = convert_speed(value_speed, from_unit_speed, to_unit_speed)

        if converted_value_speed is None:
            st.error("Invalid conversion units")
        else:
            result_speed = f"{value_speed} {from_unit_speed} = {converted_value_speed} {to_unit_speed}"
            st.markdown(f"<p style='text-align: center;'>{result_speed}</p>", unsafe_allow_html=True)

    with col6:
        st.title(" 🧊 Volume Conversion")
        from_unit_volume = st.selectbox("From Unit", list(conversion_factors_volume.keys()))
        to_unit_volume = st.selectbox("To Unit", list(conversion_factors_volume.keys()))

        value_volume = st.number_input("Enter Value",key="value_volume")

        converted_value_volume = convert_volume(value_volume, from_unit_volume, to_unit_volume)

        if converted_value_volume is None:
            st.error("Invalid conversion units")
        else:
            result_volume = f"{value_volume} {from_unit_volume} = {converted_value_volume} {to_unit_volume}"
            st.markdown(f"<p style='text-align: center;'>{result_volume}</p>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
<?php

/**
 * cp1250 encoding functions
 *
 * takes a string of unicode entities and converts it to a cp1250 encoded string
 * Unsupported characters are replaced with ?.
 *
 * @license http://opensource.org/licenses/gpl-license.php GNU Public License
 * @package squirrelmail
 * @subpackage encode
 */

/**
 * Converts string to cp1250
 * @param string $string text with numeric unicode entities
 * @return string cp1250 encoded text
 */
function charset_encode_cp1250 ($string) {
   // don't run encoding function, if there is no encoded characters
   if (! preg_match("'&#[0-9]+;'",$string) ) return $string;

    $string=preg_replace("/&#([0-9]+);/e","unicodetocp1250('\\1')",$string);
    // $string=preg_replace("/&#[xX]([0-9A-F]+);/e","unicodetocp1250(hexdec('\\1'))",$string);

    return $string;
}

/**
 * Return cp1250 symbol when unicode character number is provided
 *
 * This function is used internally by charset_encode_cp1250
 * function. It might be unavailable to other SquirrelMail functions.
 * Don't use it or make sure, that functions/encode/cp1250.php is
 * included.
 *
 * @param int $var decimal unicode value
 * @return string cp1250 character
 */
function unicodetocp1250($var) {

    $cp1250chars=array('160'=> "\xA0",
                       '164'=> "\xA4",
                       '166'=> "\xA6",
                       '167'=> "\xA7",
                       '168'=> "\xA8",
                       '169'=> "\xA9",
                       '171'=> "\xAB",
                       '172'=> "\xAC",
                       '173'=> "\xAD",
                       '174'=> "\xAE",
                       '176'=> "\xB0",
                       '177'=> "\xB1",
                       '180'=> "\xB4",
                       '181'=> "\xB5",
                       '182'=> "\xB6",
                       '183'=> "\xB7",
                       '184'=> "\xB8",
                       '187'=> "\xBB",
                       '193'=> "\xC1",
                       '194'=> "\xC2",
                       '196'=> "\xC4",
                       '199'=> "\xC7",
                       '201'=> "\xC9",
                       '203'=> "\xCB",
                       '205'=> "\xCD",
                       '206'=> "\xCE",
                       '211'=> "\xD3",
                       '212'=> "\xD4",
                       '214'=> "\xD6",
                       '215'=> "\xD7",
                       '218'=> "\xDA",
                       '220'=> "\xDC",
                       '221'=> "\xDD",
                       '223'=> "\xDF",
                       '225'=> "\xE1",
                       '226'=> "\xE2",
                       '228'=> "\xE4",
                       '231'=> "\xE7",
                       '233'=> "\xE9",
                       '235'=> "\xEB",
                       '237'=> "\xED",
                       '238'=> "\xEE",
                       '243'=> "\xF3",
                       '244'=> "\xF4",
                       '246'=> "\xF6",
                       '247'=> "\xF7",
                       '250'=> "\xFA",
                       '252'=> "\xFC",
                       '253'=> "\xFD",
                       '258'=> "\xC3",
                       '259'=> "\xE3",
                       '260'=> "\xA5",
                       '261'=> "\xB9",
                       '262'=> "\xC6",
                       '263'=> "\xE6",
                       '268'=> "\xC8",
                       '269'=> "\xE8",
                       '270'=> "\xCF",
                       '271'=> "\xEF",
                       '272'=> "\xD0",
                       '273'=> "\xF0",
                       '280'=> "\xCA",
                       '281'=> "\xEA",
                       '282'=> "\xCC",
                       '283'=> "\xEC",
                       '313'=> "\xC5",
                       '314'=> "\xE5",
                       '317'=> "\xBC",
                       '318'=> "\xBE",
                       '321'=> "\xA3",
                       '322'=> "\xB3",
                       '323'=> "\xD1",
                       '324'=> "\xF1",
                       '327'=> "\xD2",
                       '328'=> "\xF2",
                       '336'=> "\xD5",
                       '337'=> "\xF5",
                       '340'=> "\xC0",
                       '341'=> "\xE0",
                       '344'=> "\xD8",
                       '345'=> "\xF8",
                       '346'=> "\x8C",
                       '347'=> "\x9C",
                       '350'=> "\xAA",
                       '351'=> "\xBA",
                       '352'=> "\x8A",
                       '353'=> "\x9A",
                       '354'=> "\xDE",
                       '355'=> "\xFE",
                       '356'=> "\x8D",
                       '357'=> "\x9D",
                       '366'=> "\xD9",
                       '367'=> "\xF9",
                       '368'=> "\xDB",
                       '369'=> "\xFB",
                       '377'=> "\x8F",
                       '378'=> "\x9F",
                       '379'=> "\xAF",
                       '380'=> "\xBF",
                       '381'=> "\x8E",
                       '382'=> "\x9E",
                       '711'=> "\xA1",
                       '728'=> "\xA2",
                       '729'=> "\xFF",
                       '731'=> "\xB2",
                       '733'=> "\xBD",
                       '8211'=> "\x96",
                       '8212'=> "\x97",
                       '8216'=> "\x91",
                       '8217'=> "\x92",
                       '8218'=> "\x82",
                       '8220'=> "\x93",
                       '8221'=> "\x94",
                       '8222'=> "\x84",
                       '8224'=> "\x86",
                       '8225'=> "\x87",
                       '8226'=> "\x95",
                       '8230'=> "\x85",
                       '8240'=> "\x89",
                       '8249'=> "\x8B",
                       '8250'=> "\x9B",
                       '8364'=> "\x80",
                       '8482'=> "\x99",
                       '65533'=> "\x81",
                       '65533'=> "\x83",
                       '65533'=> "\x88",
                       '65533'=> "\x90",
                       '65533'=> "\x98");

    if (array_key_exists($var,$cp1250chars)) {
        $ret=$cp1250chars[$var];
    } else {
        $ret='?';
    }
    return $ret;
}
?>

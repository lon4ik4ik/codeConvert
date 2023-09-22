
    var claimRef = "VIEENT"


var airlines = '[ {  "airline": "Aeroflot - SU",  "code": "SU",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "AAS",  "code": "4i",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "Air Alsie - 6I",  "code": "6I",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "Air Cairo - SM",  "code": "SM",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "YES" },' +
'{  "airline": "Air Dolomiti - EN",  "code": "EN",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "Air Serbia - JU",  "code": "JU",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "AEGEAN ",  "code": "A3",  "VIE": "YES",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "Yes" },' +
'{  "airline": "AIS Airlines - PNX \/ IS \/ W2",  "code": "X4",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "AMERICAN AIRLINES",  "code": "AA",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "AlbaStar - AP",  "code": "AP",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "AIR FRANCE ",  "code": "AF",  "VIE": "Yes",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "Arkia - IZ",  "code": "IZ",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "Georgian Airways - A9",  "code": "A9",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "Holiday Europe - 5Q",  "code": "8Q",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "Icelandair - FI",  "code": " FI",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "BRITISH AIRWAYS",  "code": "BA",  "VIE": "YES",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "Iraqi Airways - IA",  "code": " IA",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "FLYOne",  "code": "5F",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "Israir - 6H",  "code": "6H",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "Nesma Airlines - NE",  "code": "X4",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "EUROPEAN AIR ",  "code": "BU",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "Jet2.com - LS",  "code": "LS",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "Onur Air - OHY \/ OB \/ 8Q",  "code": "8Q",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "Pobeda-DP",  "code": "DP",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "CATHAY PACIF",  "code": "CX",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "CHARLIE AIRL",  "code": "CY",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "CONDOR ",  "code": "DE",  "VIE": "Yes",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "DELTA AIRLINE",  "code": "DL",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "NORVEGIA AIR",  "code": "DY",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "ESTELAR LATIN",  "code": "E4",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "AER LINGUS",  "code": "EI",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "EMIRATES",  "code": "EK",  "VIE": "Yes",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "CSA Czech Airlines - OK",  "code": "OK",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "EUROWINGS",  "code": "EW",  "VIE": "No",  "BER": "Yes",  "DUS": "Yes",  "FRA": "Yes",  "HAM": "Yes",  "ZRH": "Yes" },' +
'{  "airline": "ETIHAD",  "code": "EY",  "VIE": "Yes",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "BULGARIA AIR",  "code": "FB",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "ISLAND AIR",  "code": "FI",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "FREE BIRD",  "code": "FH",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "Evelop ",  "code": "E9",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "GERMANIA",  "code": "GM",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "YES" },' +
'{  "airline": "Privilege - P6",  "code": "P6",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "RusLine - 7R",  "code": "7R",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "IBERIA",  "code": "IB",  "VIE": "Yes",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "AJERBAJAN ",  "code": "J2",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "AH Air Algerie",  "code": "AH",  "VIE": "Yes",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "ADRIA AIRWA",  "code": "JP",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "KOREAN AIRLI",  "code": "KE",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "Luxwing",  "code": "BN",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "AIR MALTA",  "code": "KM",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "KENYA AIRWA",  "code": "KQ",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "KUWAIT AIRW",  "code": "KU",  "VIE": "Yes",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "LUXAIR",  "code": "LG",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "LUFTHANSA",  "code": "LH",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "LIAT",  "code": "LI",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "AI Air India",  "code": "AI",  "VIE": "Yes",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "LOT POLISH ",  "code": "LO",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "Yes" },' +
'{  "airline": "SWISS",  "code": "LX",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "Siberian Airlines-S7 Airlines",  "code": "S7",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "MIDDLE EAST ",  "code": "ME",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "Fly Egypt",  "code": "FT",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "EGYPT AIR",  "code": "MS",  "VIE": "Yes",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "SmartLynx",  "code": "6Y",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "FLYPLAY",  "code": "OG",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "AUSTRIAN ",  "code": "OS",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "CROATIA AIRLI",  "code": "OU",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "PEGASUS ",  "code": "PC",  "VIE": "Yes",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "YES" },' +
'{  "airline": "Southwind Airlines",  "code": "S2",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "QATAR",  "code": "QR",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "SMART WINGS ",  "code": "QS",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "TAROM",  "code": "RO",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "ROYAL JORDA",  "code": "RJ",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "BLUE ISLAND ",  "code": "SI",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "SKANDINAVIA",  "code": "SK",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "BRUSSEL AIR",  "code": "SN",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "AEROFLOT ",  "code": "SU",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "SAUDI ARABIA",  "code": "SV",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "Utair - UT",  "code": "X4",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "ASIAN ",  "code": "T7",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "Yes" },' +
'{  "airline": "THAY AIRWAYS",  "code": "TG",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "TURKIS AIRLIN",  "code": "TK",  "VIE": "Yes",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "TAP PORTUGAL",  "code": "TP",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "AIR TRANSAT ",  "code": "TS",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "TAILWIND ",  "code": "TW",  "VIE": "Yes",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "TAILWIND ",  "code": "TI",  "VIE": "Yes",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "EASY JET ",  "code": "U2",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "Trade Air",  "code": "C3",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "AIR EUROPA",  "code": "UX",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "Ukraine International - UIA",  "code": "PS",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "TUI FLY ",  "code": "X3",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "CORENDON ",  "code": "XC",  "VIE": "Yes",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "CORENDON ",  "code": "XR",  "VIE": "Yes",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "SUN EXPRESS",  "code": "XQ",  "VIE": "Yes",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "United Airlines",  "code": "UA",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "Wings of Lebanon - W7",  "code": "W7",  "VIE": "No",  "BER": "Yes",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "EDELLWEISS ",  "code": "WK",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "OMAN AIR",  "code": "WY",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "AY Finnair",  "code": "AY",  "VIE": "Yes",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "BJ Nouvelair Tunisie",  "code": "BJ",  "VIE": "Yes",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "BZ Blue Bird",  "code": "BZ",  "VIE": "Yes",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "EI Air Lingus",  "code": "EI",  "VIE": "Yes",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "ENT Enter Air",  "code": "EN",  "VIE": "Yes",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "ET Ethopian",  "code": "ET",  "VIE": "Yes",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "HV Transavia",  "code": "HV",  "VIE": "Yes",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "Yes" },' +
'{  "airline": "J9 Jazeera",  "code": "J9",  "VIE": "Yes",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "SM Air Cairo",  "code": "SM",  "VIE": "Yes",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "Yes" },' +
'{  "airline": "SR SundAir",  "code": "SR",  "VIE": "Yes",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "TO Transavia France",  "code": "TO",  "VIE": "Yes",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "VY Yueling",  "code": "VY",  "VIE": "Yes",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "XY Flynas",  "code": "XY",  "VIE": "Yes",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "Alitalia ",  "code": "AZ",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "Yes",  "HAM": "Yes",  "ZRH": "No" },' +
'{  "airline": "Volotea",  "code": "V7",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "Yes",  "HAM": "Yes",  "ZRH": "No" },' +
'{  "airline": "KL KLM",  "code": "KL",  "VIE": "Yes",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "No" },' +
'{  "airline": "LANAR",  "code": "4M",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "Yes" },' +
'{  "airline": "Bemidji Airlines",  "code": "CH",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "Yes" },' +
'{  "airline": "MOUNT EAGLE",  "code": "MN",  "VIE": "No",  "BER": "No",  "DUS": "No",  "FRA": "No",  "HAM": "No",  "ZRH": "Yes" }]';

var airportCode = claimRef.substr(0, 3);

console.log("airportCode : " , airportCode);

var airlineCode = claimRef.substr(3, 2);

console.log("airlineCode : " , airlineCode);

var airlinesObj = JSON.parse(airlines);

console.log("airlinesObj : " , airlinesObj);

var found = airlinesObj.find(item => {
  return item.code == airlineCode
});



var supported = 'No';

if (found !== undefined) {
  switch (airportCode) {
    case 'VIE':
      supported = found.VIE;
      break;
    case 'BER':
      supported = found.BER;
      break;
    case 'DUS':
      supported = found.DUS;
      break;
    case 'FRA':
      supported = found.FRA;
      break;
    case 'HAM':
      supported = found.HAM;
      break;
    case 'ZRH':
      supported = found.ZRH;
      break;
  }
}

console.log(supported);

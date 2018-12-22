# drinks.py
# pump 1: 100ml/s, pump 2: 200ml/s, pump 3: 200ml/s, pump 4-8: 400ml/s
drink_list = [
	{
		"name": "Rum & Coke",
		"ingredients": {
			"rum": 50,
			"cola": 150
		}
	}, {
		"name": "Gin & Tonic",
		"ingredients": {
			"gin": 50,
			"tonic": 150
		}
	}, {
		"name": "Long Island",
		"ingredients": {
			"gin": 15,
			"rum": 15,
			"vodka": 15,
			"tequila": 15,
			"cola": 100,
			"oj": 30
		}
	}, {
		"name": "Screwdriver",
		"ingredients": {
			"vodka": 50,
			"oj": 150
		}
	}, {
		"name": "Margarita",
		"ingredients": {
			"tequila": 50,
			"mmix": 150
		}
	}, {
		"name": "Gin & Juice",
		"ingredients": {
			"gin": 50,
			"oj": 150
		}
	}, {
		"name": "Tequila Sunrise",
		"ingredients": {
			"tequila": 60,
			"oj": 120,
			"grenadine": 8
		}
	}, {
		"name": "Gimlet",
		"ingredients": {
			"gin": 75,
			"limejuice": 15,
			"syrup": 15
		}
	}, {
		"name": "Moscow Mule",
		"ingredients": {
			"vodka": 60,
			"gingerbeer": 90,
			"limejuice": 30
		}
	}, {
		"name": "Cosmopolitan",
		"ingredients": {
			"vodka": 45,
			"limejuice": 15,
			"cranberryjuice": 5,
			"cointreau": 30
		}
	}, {
		"name": "White Russian",
		"ingredients": {
			"vodka": 60,
			"coffeeliqeur": 30
			"cream": 20
		}
	}, {
		"name": "Tom Collins",
		"ingredients": {
			"gin": 45,
			"clubsoda": 30,
			"lemonjuice": 22,
			"syrup": 22
		}
	}, {
		"name": "Pina Colada",
		"ingredients": {
			"wrum": 45,
			"coconutcream": 60,
			"pineapplejuice": 60
		}
	}, {
		"name": "Vodka Russian",
		"ingredients": {
			"vodka": 60,
			"russianwater": 160
		}
	}, {
		"name": "Vodka Redbull",
		"ingredients": {
			"vodka": 60
		}
	}, {
		"name": "Gin Fizz",
		"ingredients": {
			"gin": 60,
			"clubsoda": 30,
			"lemonjuice": 30,
			"syrup": 22
		}
	}, {
		"name": "Sidney Icetea",
		"ingredients": {
			"cointreau": 10,
			"gin": 10,
			"peachtree": 10
			"rum": 10,
			"vodka": 10,
			"limejuice": 15,
			"cola": 100,
			"syrup": 15
		}
	}
]

drink_options = [
	{"name": "Gin", "value": "gin"},
	{"name": "Rum", "value": "rum"},
	{"name": "Vodka", "value": "vodka"},
	{"name": "Tequila", "value": "tequila"},
	{"name": "Tonic Water", "value": "tonic"},
	{"name": "Cola", "value": "cola"},
	{"name": "Orange Juice", "value": "oj"},
	{"name": "Margarita Mix", "value": "mmix"},
	{"name": "Lime Juice", "value": "limejuice"},
	{"name": "Cointreau", "value": "cointreau"},
	{"name": "White Rum", "value": "wrum"},
	{"name": "Simple Syrup", "value": "syrup"},
	{"name": "White Rum", "value": "wrum"},
	{"name": "Lemon Juice", "value": "lemonjuice"},
	{"name": "Ginger Beer", "value": "gingerbeer"},
	{"name": "Club Soda", "value": "clubsoda"},
	{"name": "Redbull", "value": "redbull"}

]

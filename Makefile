TODAY := $(shell date +%-d)
SESSION = 53616c7465645f5fde3c65cffcc30f06916497d081142fdcc42755e9d318aab29a68579fb8da0deaac6faffead3106215f450e418ea09dd9b5be8dd2ea2ae662

default: day${TODAY}-input

day%-input:
	curl -fsSL --cookie session=${SESSION} https://adventofcode.com/2022/day/$*/input > $@
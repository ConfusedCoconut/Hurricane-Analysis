# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

#2
def hurricanes_by_name(names, months, years, max_sustained_winds, areas_affected, damages_numbers, deaths):
    hurricanes = {}
    for i in range(len(names)):
        hurricanes[names[i]] = {"names": names[i],
                                "months": months[i],
                                "years": years[i],
                                "max_sustained_winds": max_sustained_winds[i],
                                "areas_affected": areas_affected[i],
                                "damages": damages_numbers[i],
                                "deaths": deaths[i]
                                }
    return hurricanes

hurricanes = hurricanes_by_name(names, months, years, max_sustained_winds, areas_affected, damages_numbers,deaths)


# 3
# create a new dictionary of hurricanes with year and key
def hurricanes_by_year(names, months, years, max_sustained_winds, areas_affected, damages_numbers, deaths):
    hurricanes = {}
    for i in range(len(names)):
        hurricanes[years[i]] = {"names": names[i],
                                "months": months[i],
                                "years": years[i],
                                "max_sustained_winds": max_sustained_winds[i],
                                "areas_affected": areas_affected[i],
                                "damages": damages_numbers[i],
                                "deaths": deaths[i]
                                }
    return hurricanes

hurricanes_year = hurricanes_by_year(names, months, years, max_sustained_winds, areas_affected, damages_numbers,deaths)


#4
# Counting Damaged Areas
# create dictionary of areas to store the number of hurricanes involved in
def damage_areas_count(areas_affected):
    area_count = {}
    for areas in areas_affected:
        for area in areas:
            if area in area_count:
                area_count[area] += 1
            else:
                area_count[area] = 1
    return area_count

areas_affected_count = damage_areas_count(areas_affected)


# 5
# Calculating Maximum Hurricane Count
# find most frequently affected area and the number of hurricanes involved in
def most_affected(dictionary):
    most = 0
    for count in dictionary.values():
        if count > most:
            most = count
    most_affected = [key for key, value in dictionary.items() if value == most]
    return most_affected, most

most_affected, most = (most_affected(areas_affected_count))
#print(''.join(most_affected) + " is the most affected are with a total of " + str(most) + " hurricanes affecting it")


# 6
# Calculating the Deadliest Hurricane
def greates_deaths(hurricanes):
    deaths = 0
    deadliest_hurricane = ""
    for i in range(len(names)):
        if hurricanes[names[i]]['deaths'] > deaths:
            deaths = hurricanes[names[i]]['deaths']
            deadliest_hurricane = hurricanes[names[i]]['names']
    return deadliest_hurricane, deaths

name, deaths = greates_deaths(hurricanes)
#print(name, deaths)


# 7
# Rating Hurricanes by Mortality
def mortality_ratings(hurricanes):
    mortality_ratings = {0: [],
        1: [],
        2: [],
        3: [],
        4: []
        }
    for i in range(len(names)):
        if hurricanes[names[i]]['deaths'] <= 100:
            rating = 0
        elif hurricanes[names[i]]['deaths'] > 100 and hurricanes[names[i]]['deaths'] <= 500:
            rating = 1
        elif hurricanes[names[i]]['deaths'] > 500 and hurricanes[names[i]]['deaths'] <= 1000:
            rating = 2
        elif hurricanes[names[i]]['deaths'] > 1000 and hurricanes[names[i]]['deaths'] <= 10000:
            rating = 3
        else:
            rating = 4
        mortality_ratings[rating].append(hurricanes[names[i]]['names'])
    return mortality_ratings

#mortality_ratings(hurricanes)


# 8
# Calculating Hurricane Maximum Damage
def greates_damage(hurricanes):
    damage = 0
    destructive_hurricane = ""
    for i in range(len(names)):
        if isinstance(hurricanes[names[i]]['damages'], str):
            continue
        elif hurricanes[names[i]]['damages'] > damage:
            damage = hurricanes[names[i]]['damages']
            destructive_hurricane = hurricanes[names[i]]['names']
    return destructive_hurricane, damage

name, damage = greates_damage(hurricanes)
#print(name, damage)


# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
def damage_ratings(hurricanes):
    damage_ratings = {0: [],
        1: [],
        2: [],
        3: [],
        4: []
        }
    for i in range(len(names)):
        if isinstance(hurricanes[names[i]]['damages'], str):
            continue
        else:
            if hurricanes[names[i]]['damages'] <= 100000000:
                rating = 0
            elif hurricanes[names[i]]['damages'] > 100000000 and hurricanes[names[i]]['damages'] <= 1000000000:
                rating = 1
            elif hurricanes[names[i]]['damages'] > 1000000000 and hurricanes[names[i]]['damages'] <= 10000000000:
                rating = 2
            elif hurricanes[names[i]]['damages'] > 10000000000 and hurricanes[names[i]]['damages'] <= 50000000000:
                rating = 3
            else:
                rating = 4
        damage_ratings[rating].append(hurricanes[names[i]]['names'])
    return damage_ratings

#damage_ratings(hurricanes)


#10
# Created a function with an additional variable that indicates the metric to group the hurricanes with.
def hurricane_rating(hurricanes, metric):
    if metric.lower() == 'damages':
        damage_ratings = {0: [],
        1: [],
        2: [],
        3: [],
        4: []
        }
        for i in range(len(names)):
            if isinstance(hurricanes[names[i]]['damages'], str):
                continue
            else:
                if hurricanes[names[i]]['damages'] <= 100000000:
                    rating = 0
                elif hurricanes[names[i]]['damages'] > 100000000 and hurricanes[names[i]]['damages'] <= 1000000000:
                    rating = 1
                elif hurricanes[names[i]]['damages'] > 1000000000 and hurricanes[names[i]]['damages'] <= 10000000000:
                    rating = 2
                elif hurricanes[names[i]]['damages'] > 10000000000 and hurricanes[names[i]]['damages'] <= 50000000000:
                    rating = 3
                else:
                    rating = 4
            damage_ratings[rating].append(hurricanes[names[i]]['names'])
        return damage_ratings
    elif metric.lower() == 'deaths':
        mortality_ratings = {0: [],
        1: [],
        2: [],
        3: [],
        4: []
        }
        for i in range(len(names)):
            if hurricanes[names[i]]['deaths'] <= 100:
                rating = 0
            elif hurricanes[names[i]]['deaths'] > 100 and hurricanes[names[i]]['deaths'] <= 500:
                rating = 1
            elif hurricanes[names[i]]['deaths'] > 500 and hurricanes[names[i]]['deaths'] <= 1000:
                rating = 2
            elif hurricanes[names[i]]['deaths'] > 1000 and hurricanes[names[i]]['deaths'] <= 10000:
                rating = 3
            else:
                rating = 4
            mortality_ratings[rating].append(hurricanes[names[i]]['names'])
        return mortality_ratings

#hurricane_rating(hurricanes, 'deaths')



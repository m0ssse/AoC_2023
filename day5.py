class Solution:
    def __init__(self, fname):
        self.read_input(fname)

    def read_input(self, fname):
        with open(fname) as inputfile:
            self.seeds, self.seed_to_soil, self.soil_to_fert, self.fert_to_water, self.water_to_light, self.light_to_temp, self.temp_to_hum, self.hum_to_loc = inputfile.read().split("\n\n")
        self.seeds=[int(x) for x in self.seeds.split(": ")[1].split()]
        self.seed_to_soil=[[int(x) for x in row.split()] for row in self.seed_to_soil.split("\n")[1:]]
        self.soil_to_fert=[[int(x) for x in row.split()] for row in self.soil_to_fert.split("\n")[1:]]
        self.fert_to_water=[[int(x) for x in row.split()] for row in self.fert_to_water.split("\n")[1:]]
        self.water_to_light=[[int(x) for x in row.split()] for row in self.water_to_light.split("\n")[1:]]
        self.light_to_temp=[[int(x) for x in row.split()] for row in self.light_to_temp.split("\n")[1:]]
        self.temp_to_hum=[[int(x) for x in row.split()] for row in self.temp_to_hum.split("\n")[1:]]
        self.hum_to_loc=[[int(x) for x in row.split()] for row in self.hum_to_loc.split("\n")[1:]]

        self.all_mappings=[self.seed_to_soil, self.soil_to_fert, self.fert_to_water, self.water_to_light, self.light_to_temp, self.temp_to_hum, self.hum_to_loc]
        for mapping in self.all_mappings:
            mapping.sort(key=lambda x: x[1])
            for inputrange in mapping:
                print(inputrange)
            print()
    def source_to_dest(self, mappings, x):
        for range_d_start, range_s_start, range_l in mappings:
            if range_s_start<=x<range_s_start+range_l:
                return range_d_start+x-range_s_start
        return x
    
    def x_to_loc(self, x):
        for mapping in self.all_mappings:
            x=self.source_to_dest(mapping, x)
        return x
    
    def solve_part1(self):
        res=float("inf")
        for seed in self.seeds:
            res=min(res, self.x_to_loc(seed))
        return res
    
    def divide_input_range(self, input_range, mapping):
        """this method breaks down a given input range into subranges such that each element in a given subrange has the same offset in the mapping"""
        res=[]
        while True:
            for _, range_s_start, range_w in mapping:
                if input_range[0]<=range_s_start<=input_range[1]:
                    res.append([input_range[0], range_s_start-1])
                    if input_range[0]<=range_s_start<=input_range[1]:
                        res.append([range_s_start, range_s_start+range_w-1])
                        input_range[0]=range_s_start+range_w
                        break
                    else:
                        res.append([range_s_start, input_range[1]])
                        return res


if __name__=="__main__":
    fname="day5_input.txt"
    sol=Solution(fname)
    print(sol.solve_part1())

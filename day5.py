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
    
    def divide_input_range2(self, input_range, mapping):
        res=[]
        changed=True
        while changed:
            a, b = input_range
            changed=False
            for _, range_start, range_w in mapping:
                c, d = range_start, range_start+range_w-1
                if b<c: #no overlap
                    #print("no overlap")
                    continue
                elif d<a:
                    #print("no overlap")
                    continue
                elif a<=c<=d<=b: #mapping range completely contained within input range
                    #print(f"mapping range {[c, d]} fully contained in input range {[a, b]}")
                    res.append([a, c-1])
                    input_range[0]=d+1
                    changed=True
                    break
                elif c<=a<=b<=d: #input range contained within mapping range
                    #print(f"input range {[a, b]} fully contained in mapping range {[c, d]}")
                    res.append([a, b])
                    return res
                elif a<=c<=b<=d:
                    #partial overlap 1
                    #print("partial overlap")
                    res.append([a, c-1])
                    input_range[0]=c
                    changed=True
                    break
                elif c<=a<=d<=b:
                    #print("partial overlap")
                    res.append([a, d])
                    input_range[0]=d+1
                    changed=True
                    break
        if not res:
            return [input_range]
        return res

    def part2(self):
        seed_ranges=[]
        for i in range(0, len(self.seeds), 2):
            seed_ranges.append([self.seeds[i], self.seeds[i]+self.seeds[i+1]-1])
        prev_ranges=seed_ranges
        for i,  mapping in enumerate(self.all_mappings):
            prev_ranges_split=[]
            new_ranges=[]

            for elem in prev_ranges:
                elem_split=self.divide_input_range2(elem, mapping)
                for elem2 in elem_split:
                    prev_ranges_split.append(elem2)
            for a, b in prev_ranges_split:
                c, d = self.source_to_dest(mapping, a), self.source_to_dest(mapping, b)
                new_ranges.append([c, d])
            prev_ranges=new_ranges
        res=[]
        for a, b in new_ranges:
            res.append(a)
            res.append(b)
        res=sorted(set(res))
        for num in res:
            print(num)

if __name__=="__main__":
    fname="day5_input.txt"
    sol=Solution(fname)
    sol.part2()

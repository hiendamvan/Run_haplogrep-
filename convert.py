#TODO:  convert json to hsd format
'''
Africa01        "16024-16569 ; 1-576 ;"         16129A  16169T  16172C  16187T  16189C  16223T  16230G  16278T  16311C 16325C                                          16327T   16354T  16368C  73G     146C    152C    185A    189G    199C    207A    247A    263G    315.1C
'''
import sys
import json
import os

# make a class for each intervals
intervals = []
class Interval:
     def __init__(self, start, end, variants):
        self.start = start
        self.end = end
        self.variants = variants

#read file json
def read_json(file):
    
    # Lấy tên file (không có phần mở rộng)
    file_id = os.path.splitext(os.path.basename(file))[0]

    with open(file) as f:
        data = json.load(f)

    # print each element on dict
    for key, value in data['intervals'].items():
        # create a new interval
        new_interval = Interval(start=value[0][0], end=value[0][1], variants=[])
        intervals.append(new_interval)

    # add variants to each interval, add enumeration to get the index
    print(type(data['variants']))
    for i, (key, value) in enumerate(data['variants'].items()):
        # to do: for each list in value, retrieve only pos and seq
        for j in value:
            intervals[i].variants.append(str(j['pos']) +  str(j['seq'] if j['seq'] != '-' else 'DEL'))    

def write_hsd(file):
    # get the name of the file
    name = file.split('.')[0]
    # Tạo thư mục nếu chưa tồn tại
    output_folder = "output_hsd"
    os.makedirs(output_folder, exist_ok=True)  
    os.makedirs("output_haplogrep", exist_ok=True)
    output_path = os.path.join(output_folder, f"output{name}.hsd")
    
    with open(output_path, 'w') as f:
        # write name
        f.write(str(name) +'\t')

        # write sequence
        f.write('"')

        for i in intervals:
            f.write(str(i.start) + '-' + str(i.end) + ' ;')
            if i == intervals[-1]:
                f.write('"\t')
            else:
                f.write(' ')

        # write variants
        for i in intervals:
            for v in i.variants:
                f.write(v + ' ')
            f.write('\t')

# main 
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert.py <input_file> <output_file>")
        sys.exit(1)

    read_json(sys.argv[1])
    write_hsd(sys.argv[2])
#print intervals


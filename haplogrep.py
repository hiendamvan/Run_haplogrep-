import sys
import subprocess

def run_haplogrep(input_file, output_file, tree_version="phylotree-rcrs@17.2"):
    command = [
        "bash", "haplogrep3", "classify",
        "--input", input_file,
        "--output", output_file,
        "--tree", tree_version
    ]
    
    subprocess.run(command, check=True)
    print(f"Kết quả HaploGrep lưu tại: {output_file}")
    #TODO: if input file has some error: 

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
        sys.exit(1)

    run_haplogrep(sys.argv[1], sys.argv[2])


## Run on CLI
#python3 haplogrep.py <input> <output> 

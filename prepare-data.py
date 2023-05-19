import json
def main():
  colors = [x.strip() for x in readfile('assets/colors.txt')]
  cities  = [x.strip() for x in readfile('assets/cities.txt')]
  dest = {}
  
  outFile = open('training-data.jsonl', 'w')
  
  for city in cities:
    initial = city[0].lower()
    color = colors[ord(initial) - ord('a')]
    print(city, initial, color)
    data = {
      'prompt': city,
      'completion': color.strip().lower(),
    }
    outFile.write(json.dumps(data))
    outFile.write("\n")
    
  outFile.close()
  
  
def readfile(filename):
  with open(filename, 'r') as f:
    lines = f.readlines()
  return lines

main()
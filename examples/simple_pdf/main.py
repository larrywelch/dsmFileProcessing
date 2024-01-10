from pdfLib import myFunctions

print('Simple Use of PDF Library')

def test_haversine():
  print('executing test...')
  
    # Amsterdam to Berlin
  assert myFunctions.haversine(
        4.895168, 52.370216, 13.404954, 52.520008
    ) == 576.6625818456291
    
test_haversine()

print('Complete.')
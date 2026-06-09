num = float(input(""))

int0_25 = 0
int26_50 = 0
int51_75 = 0
int76_100 = 0

while num >= 0:
  
    if num >= 0 and num <= 25:
        int0_25 += 1
    else:
        if num >= 26 and num <= 50:
            int26_50 += 1
        else: 
            if num >= 51 and num <= 75:
                int51_75 += 1
            else:
                if num <= 100:
                    int76_100 += 1
                    
    num = float(input(""))

print(int0_25, int26_50, int51_75, int76_100)


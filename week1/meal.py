def main():
    a = [
        {"meal": "breakfast time", "start hour":7 ,"end hour":8},
        {"meal": "lunch time", "start hour":12 ,"end hour":13},
        {"meal": "dinner time", "start hour":18 ,"end hour":19},
    ]
    time=input("what time is it ?")
    time=float(convert(time))
    for document in a :
        if time >= float(document["start hour"]) and time <= float(document["end hour"]):
            print(document["meal"])

def convert(time):
    c=0.0
    if time.rfind(" a.m. ") != -1:
        time=time.replace("a.m.","")
    elif time.rfind(" a.m. ") != -1:
        time=time.replace(" p.m.","")
        c=12.0

    h,m =time.strip().split(":")
    t=float(h)+ c + (float(m))/60
    return t

if __name__ == "__main__":
    main()
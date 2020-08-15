class actor:
    name = "Milady"
    sex = "female"
    height = 169
    locate = "Mage"
    race = "human"

    # skill = "jixiepucong"
    # skill1 = "kongzhongzhiyuan"
    # skill2 = "qiangzhiruqin"
    # skill3 = "haojiecichang"


    def walk(self,a):
        # walk = "还有5秒到达战场"
        print("还有5秒到达战场")

    def arrive(self):
        # arrive = "到达战场"
        print("到达战场")

    def hit(self):
        # hit = "补刀"
        print("补兵")

    def fight(self):
        # fight = "对战敌方英雄"
        print("对战敌方英雄")


Milady = actor()
print(actor.name)
print(actor.race)
print(actor.locate)
# print(actor.walk("还有5秒到达战场"))


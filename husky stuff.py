#create class and def lengths and classeas 

class Dog:
    def __init__(self, arm_length: float, leg_length: float, num_eyes: int,
                 has_tail: bool, is_furry: bool):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry
#self. refers to class and returns the correct bool? right>
    def describe(self):
        print("==- Siberian Husky Physical Characteristics ===")
        print(f"  Arm length:  {self.arm_length} inches")
        print(f"  Leg length:  {self.leg_length} inches")
        print(f"  Number of eyes: {self.num_eyes}")
        print(f"  Has a tail:  {'Yes' if self.has_tail else 'No'}")
        print(f"  Is furry:    {'Yes' if self.is_furry else 'No'}")

#main function to print
def main():
    # husky phys values?? maybe idk
    husky = Dog(
        arm_length=10.5,   # front leg/arm length in inches
        leg_length=16.0,   # rear leg length in inches
        num_eyes=2,
        has_tail=True,
        is_furry=True
    )
    husky.describe()


if __name__ == "__main__":
    main()
class Country:
    def __init__(self, country, nationality):
        self.countryName = country
        self.nationality = nationality
    
    def printCountry(self):
        print(f"Country => {self.countryName}")

    def printNationality(self):
        print(f"Nationality => {self.nationality}")

class State(Country):
    def __init__(self, country, nationality, state):
        super().__init__(country, nationality)
        self.stateName = state

    def printState(self):
        print(f"State => {self.stateName}")

    def printDetails(self):
        self.printCountry()
        self.printNationality()
        self.printState()

inputCountryName = input("Enter Country Name: ")
inputNationality = input("Enter Nationality: ")
inputStateName = input("Enter State Name: ")

stateObj = State(inputCountryName, inputNationality, inputStateName)
stateObj.printDetails()
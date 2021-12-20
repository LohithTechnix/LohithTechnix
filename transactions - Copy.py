

class Transactions():
    def __init__(self,bal):
        self.bal=bal
        self.statement={'Description':['Initial balance'], 'amount':[], 'Balance':[bal]}
    def command(self):
        money = input("?")
        #add command description to the dictionary
        #based on first letter call respective function
        #t 23 or r 34 or b or q
        while money!='q':
            if 't' in money:
                self.statement['Description'].append('Top up')
                self.top_up(int(money.split()[1]))

            elif 'r' in money:
                self.statement['Description'].append('Ride')
                self.ride(int(money.split()[1]))
                
            elif 'b' in money:
                print(self.balance())
            money = input("?")
        self.display()
        
        
            
    def top_up(self,amnt):
        #add the amnt
        self.bal+=amnt
        self.statement['amount'].append(amnt)
        self.statement['Balance'].append(self.bal)

    def ride(self,amnt):
        #deduct the amnt
        self.bal-=amnt
        self.statement['amount'].append(amnt)
        self.statement['Balance'].append(self.bal)

    def balance(self):
        return self.bal

    def display(self):
        df= pd.DataFrame(self.statement)
        print(df)
        exit()


    
trans=Transactions(int(input(('Initial balance'))))  
trans.command()

                    



        

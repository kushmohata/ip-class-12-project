import pandas as pd
import matplotlib.pyplot as plt

choice=[1,2,3,4,5,6,7,8,9]
for val in choice:
    print("                                MENU")
    print("                Press  1 TO Add Data")
    print("                Press  2 TO Delete Data")
    print("                Press  3 TO See DataFrame Of Bitcoin ")
    print("                Press  4 TO See Graph Of Bitcoin ")
    print("                Press  5 TO See DataFrame Of Ethereum ")
    print("                Press  6 TO See Graph Of Ethereum ")
    print("                Press  7 TO See DataFrame Of Axie Infinity")
    print("                Press  8 TO See Graph Of Axie Infinity")
    print("                Press  9 TO Compare Graph ")
    print("                Press 10 TO Open Investment Calculator")
    print("                Press 11 TO EXIT")
    
 
    val=int(input("Enter Value"))
    if val==1:
        print("                                SUB-MENU")
        print("                Press 1 TO Enter Data Of Bitcoin")
        print("                Press 2 TO Enter Data Of Ethereum ")
        print("                Press 3 TO Enter Data Of Axie Infinity")
        print("                Press Any Other Numeric Key TO Go Back")
        CH=int(input("Enter Value"))
        if CH==1:
            rec=int(input("How Many Records You Want To Insert"))
            for x in range(rec):
                date,price,ope,high,low,vol,per=input(
                "Enter Row Of Data You Want To Add").split()
                b=pd.read_csv('D:\\ip project\\btc.csv',index_col='Date')
                btc=pd.DataFrame(b)
                btc.at[date,:]=[price,ope,high,low,vol,per]
                btc.to_csv('D:\\ip project\\btc.csv')
            else:
                k=pd.read_csv('D:\\ip project\\btc.csv',index_col='Date')
                btc=pd.DataFrame(k)
                print(btc)
        elif CH==2:
            rec=int(input("How Many Records You Want To Insert"))
            for x in range(rec):
                date,price,ope,high,low,vol,per=input(
                "Enter Row Of Data You Want To Add").split()
                e=pd.read_csv('D:\\ip project\\ethereum.csv',index_col='Date')
                eth=pd.DataFrame(e)
                eth.at[date,:]=[price,ope,high,low,vol,per]
                eth.to_csv('D:\\ip project\\ethereum.csv')
            else:
                e=pd.read_csv('D:\\ip project\\ethereum.csv',index_col='Date')
                eth=pd.DataFrame(e)
                print(eth)
        elif CH==3:
            rec=int(input("How Many Records You Want To Insert"))
            for x in range(rec):
                date,price,ope,high,low,vol,per=input(
                "Enter Row Of Data You Want To Add").split()
                a=pd.read_csv('D:\\ip project\\axie.csv',index_col='Date')
                axie=pd.DataFrame(a)
                axie.at[date,:]=[price,ope,high,low,vol,per]
                axie.to_csv('D:\\ip project\\axie.csv')
            else:
                a=pd.read_csv('D:\\ip project\\axie.csv',index_col='Date')
                axie=pd.DataFrame(a)
                print(axie)
        else:
            print()
    if val==2:
        print("                                SUB-MENU")
        print("                Press 1 TO Delete Data Of Bitcoin")
        print("                Press 2 TO Delete Data Of Ethereum ")
        print("                Press 3 TO Delete Data Of Axie Infinity")
        print("                Press Any Other Key TO Go Back")
        Ch=int(input("Enter Value"))
        if Ch==1:
            rec=int(input("How Many Records You Want To Delete"))
            for x in range(rec):
                date=str(input("Enter Month"))
                k=pd.read_csv('D:\\ip project\\btc.csv',index_col='Date')
                btc=pd.DataFrame(k)
                btc=btc.drop(date)
                btc.to_csv('D:\\ip project\\btc.csv')
            else:
                k=pd.read_csv('D:\\ip project\\btc.csv',index_col='Date')
                btc=pd.DataFrame(k)
                print(btc)
        elif Ch==2:
            rec=int(input("How Many Records You Want To Delete"))
            for x in range(rec):
                date=str(input("Enter Month"))
                e=pd.read_csv('D:\\ip project\\ethereum.csv',index_col='Date')
                eth=pd.DataFrame(e)
                eth=eth.drop(date)
                eth.to_csv('D:\\ip project\\ethereum.csv')
            else:
                e=pd.read_csv('D:\\ip project\\ethereum.csv',index_col='Date')
                eth=pd.DataFrame(e)
                print(eth)
        elif Ch==3:
            rec=int(input("How Many Records You Want To Delete"))
            for x in range(rec):
                date=str(input("Enter Month"))
                a=pd.read_csv('D:\\ip project\\axie.csv',index_col='Date')
                axie=pd.DataFrame(a)
                axie=axie.drop(date)
                axie.to_csv('D:\\ip project\\axie.csv')
            else:
                a=pd.read_csv('D:\\ip project\\axie.csv',index_col='Date')
                axie=pd.DataFrame(a)
                print(axie)
        else:
            
            print()
        
    if val==3:
        btc=pd.read_csv('D:\\ip project\\btc.csv',index_col='Date')
        k=pd.DataFrame(btc)
        print(k)
    elif val==4:
        k=pd.read_csv('D:\\ip project\\btc.csv')
        btc=pd.DataFrame(k)
        x=(pd.Series(btc.loc[:,'Date'])).iloc[0:48:2]
        y=(pd.Series(btc.loc[:,'Price'])).iloc[0:48:2]
        plt.plot(x,y,color='green',label='Bitcoin')
        plt.title('BITCOIN ( PRICE VS MONTH )')
        plt.xlabel('Month')
        plt.ylabel('Price')
        plt.legend(loc='upper left')
        plt.show()
    elif val==5:
        a=pd.read_csv('D:\\ip project\\ethereum.csv',index_col='Date')
        eth=pd.DataFrame(a)
        print(eth)
    elif val==6:
        a=pd.read_csv('D:\\ip project\\ethereum.csv')
        eth=pd.DataFrame(a)
        x=(pd.Series(eth.loc[:,'Date'])).iloc[0:48:2]
        y=(pd.Series(eth.loc[:,'Price'])).iloc[0:48:2]
        plt.plot(x,y,color='blue',label='ETHEREUM')
        plt.title('ETHEREUM ( PRICE VS MONTH )')
        plt.xlabel('Month')
        plt.ylabel('Price')
        plt.legend(loc='upper left')
        plt.show()
        
    elif val==7:
        df=pd.read_csv('D:\\ip project\\axie.csv',index_col='Date')
        axie=pd.DataFrame(df)
        print(axie)
    elif val==8:
        df=pd.read_csv('D:\\ip project\\axie.csv')
        axie=pd.DataFrame(df)
        x=(pd.Series(axie.loc[:,'Date'])).iloc[0:48:2]
        y=(pd.Series(axie.loc[:,'Price'])).iloc[0:48:2]
        plt.plot(x,y,color='red',label='AXIE INFINITY')
        plt.title('AXIE INFINITY ( PRICE VS MONTH )')
        plt.xlabel('Month')
        plt.ylabel('Price')
        plt.legend(loc='upper left')
        plt.show()
        
    elif val==9:
       choice=[1,2,3,4,5,6,7,8,9]
       for val in choice:
           print("Press 1 For Bitcoin VS Ethereum")
           print("Press 2 For Ethereum VS Axie Infinity")
           print("Press 3 For Bitcoin VS Ethereum VS Axie Infinity")
           print("Press 4 To Show Graph Of 5 Cryptocurrency")
           print("Press Any Other Numeric Key TO Go Back")
           ch=int(input("Choose The Graph Which You Want To See"))
           if ch==1:
               k=pd.read_csv('D:\\ip project\\btc.csv')
               btc=pd.DataFrame(k)
               a=pd.read_csv('D:\\ip project\\ethereum.csv')
               eth=pd.DataFrame(a)
               l=eth.index[-1]+1
               x=(pd.Series(btc.loc[:,'Date'])).iloc[0:l:2]
               y=(pd.Series(btc.loc[:,'Percent'])).iloc[0:l:2]
               y1=(pd.Series(eth.loc[:,'Percent'])).iloc[0:l:2]
               plt.plot(x,y,color='green',label='Bitcoin')
               plt.plot(x,y1,color='blue',label='Ethereum')
               plt.title('   Bitcoin VS Ethereum')
               plt.xlabel('Month')
               plt.ylabel('Percent')
               plt.legend(loc='upper left')
               plt.show()
           elif ch==2:
                a=pd.read_csv('D:\\ip project\\ethereum.csv')
                eth=pd.DataFrame(a)
                df=pd.read_csv('D:\\ip project\\axie.csv')
                axie=pd.DataFrame(df)
                l=eth.index[-1]+1
                x=(pd.Series(eth.loc[:,'Date'])).loc[33:l]
                y=(pd.Series(eth.loc[:,'Percent'])).loc[33:l]
                y1=pd.Series(axie.loc[:,'Percent'])
                plt.plot(x,y,color='blue',label='Ethereum')
                plt.plot(x,y1,color='red',label='Axie Infinity')
                plt.title('   Ethereum VS Axie Infinity')
                plt.xlabel('Month')
                plt.ylabel('Percent')
                plt.legend(loc='upper left')
                plt.show()
           elif ch==3:
                df=pd.read_csv('D:\\ip project\\axie.csv')
                a=pd.read_csv('D:\\ip project\\ethereum.csv')
                k=pd.read_csv('D:\\ip project\\btc.csv')
                btc=pd.DataFrame(k)
                eth=pd.DataFrame(a)
                axie=pd.DataFrame(df)
                l=btc.index[-1]+1
                x=(pd.Series(btc.loc[:,'Date'])).iloc[33:l]
                y=(pd.Series(btc.loc[:,'Percent'])).iloc[33:l]
                y1=pd.Series(eth.loc[:,'Percent']).iloc[33:l]
                y2=pd.Series(axie.loc[:,'Percent'])
                plt.plot(x,y,color='green',label='Bitcoin')
                plt.plot(x,y1,color='blue',label='Ethereum')
                plt.plot(x,y2,color='red',label='Axie Infinity')
                plt.title('   Percent VS Month')
                plt.xlabel('Month')
                plt.ylabel('Percent')
                plt.legend(loc='upper left')
                plt.show()
           elif ch==4:
                df=pd.read_csv('D:\\ip project\\axie.csv')
                a=pd.read_csv('D:\\ip project\\ethereum.csv')
                k=pd.read_csv('D:\\ip project\\btc.csv')
                m=pd.read_csv('D:\\ip project\\doge.csv')
                n=pd.read_csv('D:\\ip project\\bnb.csv')
                btc=pd.DataFrame(k)
                eth=pd.DataFrame(a)
                axie=pd.DataFrame(df)
                doge=pd.DataFrame(m)
                bnb=pd.DataFrame(n)
                l=btc.index[-1]+1
                x=(pd.Series(btc.loc[:,'Date'])).iloc[33:l]
                y=(pd.Series(btc.loc[:,'Percent'])).iloc[33:l]
                y1=pd.Series(eth.loc[:,'Percent']).iloc[33:l]
                y2=pd.Series(axie.loc[:,'Percent'])
                y3=pd.Series(doge.loc[:,'Percent']).iloc[33:l]
                y4=pd.Series(bnb.loc[:,'Percent']).iloc[33:l]
                plt.plot(x,y,color='green',label='Bitcoin')
                plt.plot(x,y1,color='blue',label='Ethereum')
                plt.plot(x,y2,color='red',label='Axie Infinity')
                plt.plot(x,y3,color='aqua',label='Doge Coin')
                plt.plot(x,y4,color='teal',label='Binance')
                plt.title('   Grwoth Percent VS Month')
                plt.xlabel('Month')
                plt.ylabel('Grwoth Percent')
                plt.legend(loc='upper right')
                plt.show()
           else:
               break
       else:
            print()
            
    elif val==10:
        choice=[1,2,3,4,5,6,7,8,9]
        for val in choice:
         print("                  INVESTMENT CALCULATOR FOR CRYPTOCURRENCY              ")
         print("Press 1 for Bitcoin")
         print("Press 2 for Ethereum")
         print("Press 3 for Axie Infinity")
         print("Press Any Other Numeric Key TO Go Back")
         a=int(input("Choose The Cryptocurrency In Which You Want To Invest"))
         if a==1:
            invest=int(input("Enter Amount Which You Want To Invest (In Rs)"))
            year=int(input("For How Many Years You Want To Invest"))
            us=int(input("Enter current price of us dollar in Rs)"))
            amt=invest/us
            cp=int(input("Enter Current Value Of Bitcoin In US Dollar"))
            btc_min=70000
            btc_max=100000
            min_per=(btc_min-cp)/cp
            max_per=(btc_max-cp)/cp
            min_profit=(min_per*amt)+amt
            max_profit=(max_per*amt)+amt
            print('Minimum Profit Expected In',year,'years',min_profit*us*year)
            print('Maximum Profit Expected In',year,'years',max_profit*us*year*2)
         elif a==2:
            invest=int(input("Enter Amount Which You Want To Invest (In Rs)"))
            year=int(input("For How Many Years You Want To Invest"))
            us=int(input("Enter current price of us dollar in Rs)"))
            amt=invest/us
            print("Your Investment Amount In Us Dollar Is",amt)
            cp=int(input("Enter Current Value Of Ethereum In US Dollar"))
            eth_min=6000
            eth_max=10000
            min_per=(eth_min-cp)/cp
            max_per=(eth_max-cp)/cp
            min_profit=(min_per*amt)+amt
            max_profit=(max_per*amt)+amt
            print('Minimum Profit Expected In',year,'years',min_profit*us*year)
            print('Maximum Profit Expected In',year,'years',max_profit*us*year*2)
         elif a==3:
            invest=int(input("Enter Amount Which You Want To Invest (In Rs)"))
            year=int(input("For How Many Years You Want To Invest"))
            us=int(input("Enter current price of us dollar in Rs)"))
            amt=invest/us
            print("Your Investment Amount In Us Dollar Is",amt)
            cp=int(input("Enter Current Value Of Axie Infinity In US Dollar"))
            axs_min=120
            axs_max=200
            min_per=(axs_min-cp)/cp
            max_per=(axs_max-cp)/cp
            min_profit=min_per*amt+amt
            max_profit=max_per*amt+amt
            print('Minimum Profit Expected In',year,'years',min_profit*us*year)
            print('Maximum Profit Expected In',year,'years',max_profit*us*year*2)
         else:
            break
        else:
            print()

      
    elif val==11:
        print('                              THANK YOU')
        break




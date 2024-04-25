import pandas as pd
import openpyxl as px

class Data:
    def __init__(self):
        pass

    def askforinputfile(self):
        self.filename = input("PLEASE ENTER THE NAME OF THE FILE WITHOUT EXTENSION==>")

    def read_file(self):

        # old method
        """
        df = pd.read_excel(
            self.filename + ".xlsx",
            header=None,
            usecols="B:D",
            skiprows=1,
            sheet_name=[
                "ST10A",
                "ST10B",
                "ST20A",
                "ST20B",
                "ST30A",
                "ST30B",
                "ST40A",
                "ST40B",
                "ST50A",
                "ST50B",
                "ST60A",
                "ST60B",
                "ST71",
                "ST72",
                "ST80",
                "ST90",
                "ST91",
                "ST92",
                "ST100",
                "ST110",
                "ST120",
            ],
        )
        #print(df)
        #print(time.time() - startime)
        """

        # this method is less readable and requires installation of openpyxl, but is ~20% faster
        sheet_names = [
            "ST10A",
            "ST10B",
            "ST20A",
            "ST20B",
            "ST30A",
            "ST30B",
            "ST40A",
            "ST40B",
            "ST50A",
            "ST50B",
            "ST60A",
            "ST60B",
            "ST71",
            "ST72",
            "ST80",
            "ST90",
            "ST91",
            "ST92",
            "ST100",
            "ST110",
            "ST120",
        ]

        local_data = px.load_workbook(self.filename + ".xlsx", read_only=True)
        local_data_dict = {}
        # convert all the data in the file into a dataframe
        for sheet in sheet_names:
            local_data_dict[sheet] = pd.DataFrame(local_data[sheet].values)
        # copy all of the data that is actually needed into a different dictionary
        # shift all the data up to emulate the behavior of read_excel, which drops the first value while still starting at row 0
        local_data_dict_trimmed = {}
        for sheet in sheet_names:
            local_data_dict_trimmed[sheet] = pd.DataFrame(local_data_dict[sheet].shift(-1).drop(local_data_dict[sheet].tail(1).index),columns=(1,2,3))

        # print(local_data_dict_trimmed)
        # print(time.time() - startime)

        self.alldata = local_data_dict_trimmed
        return local_data_dict_trimmed

    def get_productivity_count(self, data):
        data.dropna(inplace=True)

        # GETTING START TIME
        startime = data.iloc[0, 0]

        # GETTING END TIME
        endtime = data.iloc[len(data) - 1, 0]

        # FUNCTION TO COUNT PRODUCTIVITY CODE WITHIN GIVEN SPECIFIED TIME
        def countproductivity(startime, secondtime):
            return len(
                data[
                    (data[1] >= startime)
                    & (data[1] < secondtime)
                    & (data[3] == "1 - Productive")
                ]
            )

        # INITIALIZING AN ARRAY
        self.productivityarray = []
        self.timearray = []
        ignorestart = pd.Timestamp("2:30:00")
        ignoreend = pd.Timestamp("6:00:00")

        while startime < endtime:

            # if not (ignorestart.time() < startime.time() < ignoreend.time()):
            # SECOND TIME IS STARTIME + 1 HOUR
            secondtime = startime + pd.Timedelta(hours=0.5)
            # USING THE FUNCTION TO GET THE COUNT

            # checkdate is a function that checks whether the startime falls in the break period or not but it has not been implemented properly
            # a  = self.checkdate(startime)

            # if a:
            count = countproductivity(startime, secondtime)
            # INCREMENTING STARTIME BY 1 HOUR
            # IF COUNT ==0 THEN SKIP

            self.productivityarray.append(count)
            self.timearray.append(startime)
            startime += pd.Timedelta(hours=0.5)

        return [self.productivityarray, self.timearray]

    sheet_names=["ST10A","ST10B","ST20A","ST20B","ST30A","ST30B","ST40A","ST40B","ST50A",
                                             "ST50B","ST60A","ST60B","ST71","ST72","ST80","ST90","ST91","ST92","ST100","ST110","ST120"]

    global dfs
    def createDictionary(self, sheet_names):

        dfs= {}
        for name in sheet_names:
            dfs[name] = pd.DataFrame.from_dict(self.alldata[name])

        for name in sheet_names:
            dfs[name] = dfs[name].dropna()
        return dfs

    def create_dataframeforsinglemachine(self, key):
        # selecting particular machine
        machinedata = self.alldata[key]
        # getting productivity and time arrays
        a, b = self.get_productivity_count(machinedata)
        # creating a dataframe
        machinedataframe = pd.DataFrame(a, b)
        # resetting the index
        machinedataframe.reset_index(inplace=True)
        # setting appropriate column names
        machinedataframe.columns = ["index", "Value"]
        # returning df
        return machinedataframe

    def dataforml(self):
        # used for extracting data for machine learning
        return [self.productivityarray, self.timearray]

    def checkdate(self, startime):
        # doesnot work properly
        break1start = pd.Timestamp("9:20:00")
        break1end = pd.Timestamp("9:40:00")
        break2start = pd.Timestamp("12:30:00")
        break2end = pd.Timestamp("1:00:00")
        break3start = pd.Timestamp("20:00:00")
        break3end = pd.Timestamp("20:30:00")
        break4start = pd.Timestamp("23:30:00")
        break4end = pd.Timestamp("00:00:00")
        endshiftstart = pd.Timestamp("2:30:00")
        endshiftend = pd.Timestamp("6:30:00")
        weekendbreak1start = pd.Timestamp("8:40:00")
        weekendbreak1end = pd.Timestamp("9:00:00")
        weekendbreak2start = pd.Timestamp("12:30:00")
        weekendbreak2end = pd.Timestamp("1:00:00")
        weekendbreak3start = pd.Timestamp("3:40:00")
        weekendbreak3end = pd.Timestamp("4:00:00")
        startday = startime.strftime("%A")
        if startday=="Sunday" or startday=="Saturday" or startday=="Friday":
            if weekendbreak1start<=startime<=weekendbreak1end or weekendbreak2start<=startime<=weekendbreak2end or weekendbreak3start<=startime<=weekendbreak3end:
                return False

        else:
            if break1start<=startime<=break1end or break2start<=startime<=break2end or break3start<=startime<=break3end or break4start<=startime<=break4end or endshiftstart<=startime<=endshiftend:
                return False
        return True
    def getstartandenddate(self):
        data = self.alldata["ST10A"]
        data.dropna(inplace=True)

        startime = data.iloc[0, 0]

        # GETTING END TIME
        endtime = data.iloc[len(data) - 1, 0]
      
        return [startime, endtime]

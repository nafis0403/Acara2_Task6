import arcpy
arcpy.env.overwriteOutput = True

# Note: Script assumes data from Pro SDK community samples are installed under C:\Data, as follows:
inFC = "C:\Data\FeatureTest\FeatureTest.gdb\TestPoints"
outFCBuffer300 = "C:\Data\FeatureTest\FeatureTest.gdb\TestPoints_Buffer_300ft"
outFCBuffer400 = "C:\Data\FeatureTest\FeatureTest.gdb\TestPoints_Buffer_400ft"
outFCBuffer500 = "C:\Data\FeatureTest\FeatureTest.gdb\TestPoints_Buffer_500ft"

# Buffer the input features creating three buffer distance feature classes
arcpy.Buffer_analysis(inFC, outFCBuffer300, "300 feet")
arcpy.Buffer_analysis(inFC, outFCBuffer400, "400 feet")
arcpy.Buffer_analysis(inFC, outFCBuffer500, "500 feet")

# The following message will be included in the message box from the calling button's OnClick routine
print("Buffer routine from Python script complete. \r\n View and add 300-, 400- and 500-foot buffer feature classes from the Catalog pane.")

# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Unstructured Grid Reader'
myVtu = XMLUnstructuredGridReader(FileName=[sys.argv[1]])

# create a new 'Threshold'
threshold1 = Threshold(Input=myVtu)
threshold1.Scalars = ['POINTS', 'AppartientEntree1']
threshold1.ThresholdRange = [0.0, 1.0]

# Properties modified on threshold1
threshold1.Scalars = ['POINTS', 'LevelSetEntree6']
threshold1.ThresholdRange = [0.0, 100000.0]

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [2236, 1486]

# show data in view
threshold1Display = Show(threshold1, renderView1)

# trace defaults for the display properties.
threshold1Display.Representation = 'Surface'
threshold1Display.ColorArrayName = [None, '']
threshold1Display.OSPRayScaleArray = 'AppartientEntree1'
threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold1Display.SelectOrientationVectors = 'AppartientEntree1'
threshold1Display.ScaleFactor = 1.5
threshold1Display.SelectScaleArray = 'AppartientEntree1'
threshold1Display.GlyphType = 'Arrow'
threshold1Display.GlyphTableIndexArray = 'AppartientEntree1'
threshold1Display.GaussianRadius = 0.075
threshold1Display.SetScaleArray = ['POINTS', 'AppartientEntree1']
threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold1Display.OpacityArray = ['POINTS', 'AppartientEntree1']
threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
threshold1Display.SelectionCellLabelFontFile = ''
threshold1Display.SelectionPointLabelFontFile = ''
threshold1Display.PolarAxes = 'PolarAxesRepresentation'
threshold1Display.ScalarOpacityUnitDistance = 0.49362748382282323

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
threshold1Display.DataAxesGrid.XTitleFontFile = ''
threshold1Display.DataAxesGrid.YTitleFontFile = ''
threshold1Display.DataAxesGrid.ZTitleFontFile = ''
threshold1Display.DataAxesGrid.XLabelFontFile = ''
threshold1Display.DataAxesGrid.YLabelFontFile = ''
threshold1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
threshold1Display.PolarAxes.PolarAxisTitleFontFile = ''
threshold1Display.PolarAxes.PolarAxisLabelFontFile = ''
threshold1Display.PolarAxes.LastRadialAxisTextFontFile = ''
threshold1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# hide data in view
Hide(myVtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# Hide orientation axes
renderView1.OrientationAxesVisibility = 0

# get the material library
materialLibrary1 = GetMaterialLibrary()

# set scalar coloring
ColorBy(threshold1Display, ('POINTS', 'Pression'))

# rescale color and/or opacity maps used to include current data range
threshold1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
threshold1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Pression'
pressionLUT = GetColorTransferFunction('Pression')
pressionLUT.RGBPoints = [-1.005270004272461, 0.231373, 0.298039, 0.752941, -0.0241985023021698, 0.865003, 0.865003, 0.865003, 0.9568729996681213, 0.705882, 0.0156863, 0.14902]
pressionLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Pression'
pressionPWF = GetOpacityTransferFunction('Pression')
pressionPWF.Points = [-1.005270004272461, 0.0, 0.5, 0.0, 0.9568729996681213, 1.0, 0.5, 0.0]
pressionPWF.ScalarRangeInitialized = 1

# Rescale transfer function
pressionLUT.RescaleTransferFunction(-0.5, 0.5)

# Rescale transfer function
pressionPWF.RescaleTransferFunction(-0.5, 0.5)

# hide color bar/color legend
threshold1Display.SetScalarBarVisibility(renderView1, False)

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [2.5, 0.0, 10000.0]
renderView1.CameraFocalPoint = [2.5, 0.0, 0.0]
renderView1.CameraParallelScale = 5.088099246178918
renderView1.Background = [0,0,0]

# save screenshot
path = sys.argv[1].split(".")
img  = path[0].split("/")[-1]
SaveScreenshot("pressures/"+img+".png", renderView1, ImageResolution=[1070, 798])

# set scalar coloring
ColorBy(threshold1Display, ('POINTS', 'Vitesse', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pressionLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
threshold1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
threshold1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Vitesse'
vitesseLUT = GetColorTransferFunction('Vitesse')
vitesseLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.6554652424863466, 0.865003, 0.865003, 0.865003, 1.3109304849726933, 0.705882, 0.0156863, 0.14902]
vitesseLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Vitesse'
vitessePWF = GetOpacityTransferFunction('Vitesse')
vitessePWF.Points = [0.0, 0.0, 0.5, 0.0, 1.3109304849726933, 1.0, 0.5, 0.0]
vitessePWF.ScalarRangeInitialized = 1

# Rescale transfer function
vitesseLUT.RescaleTransferFunction(0.0, 1.0)

# Rescale transfer function
vitessePWF.RescaleTransferFunction(0.0, 1.0)

# Rescale transfer function
vitesseLUT.RescaleTransferFunction(0.0, 1.25)

# Rescale transfer function
vitessePWF.RescaleTransferFunction(0.0, 1.25)

# hide color bar/color legend
threshold1Display.SetScalarBarVisibility(renderView1, False)

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [2.5, 0.0, 10000.0]
renderView1.CameraFocalPoint = [2.5, 0.0, 0.0]
renderView1.CameraParallelScale = 5.088099246178918
renderView1.Background = [0,0,0]

# save screenshot
SaveScreenshot("velocities/"+img+".png", renderView1, ImageResolution=[1070, 798])

# set scalar coloring
ColorBy(threshold1Display, ('POINTS', 'AppartientEntree6'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pressionLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
threshold1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
threshold1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Vitesse'
vitesseLUT = GetColorTransferFunction('AppartientEntree6')
vitesseLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.6554652424863466, 0.865003, 0.865003, 0.865003, 1.3109304849726933, 0.705882, 0.0156863, 0.14902]
vitesseLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Vitesse'
vitessePWF = GetOpacityTransferFunction('AppartientEntree6')
vitessePWF.Points = [0.0, 0.0, 0.5, 0.0, 1.3109304849726933, 1.0, 0.5, 0.0]
vitessePWF.ScalarRangeInitialized = 1

# Rescale transfer function
vitesseLUT.RescaleTransferFunction(0.0, 1.0)

# Rescale transfer function
vitessePWF.RescaleTransferFunction(0.0, 1.0)
vitesseLUT.ApplyPreset('X Ray', True)

# hide color bar/color legend
threshold1Display.SetScalarBarVisibility(renderView1, False)

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [2.5, 0.0, 10000.0]
renderView1.CameraFocalPoint = [2.5, 0.0, 0.0]
renderView1.CameraParallelScale = 5.088099246178918
renderView1.Background = [0,0,0]

# save screenshot
SaveScreenshot("shapes/"+img+".png", renderView1, ImageResolution=[1070, 798])

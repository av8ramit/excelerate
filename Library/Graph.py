####################################################################################################################################################  
#                                                                                                                                                  #
# This file has been generated by Amit Patankar:                                                                                                   #
#     Created by              : amit.patankar                                                                                                      #    
#     Created on              : 08-08-2013                                                                                                         #
#     Directory               : /Desktop/                                                                                                          #
#     Purpose                 : This file represents a data graph.                                                                                 #
#                                                                                                                                                  #
#################################################################################################################################################### 

from Values import *
from User import *
class Graph(object):

    def __init__(self, name, index, points, averages = None, overallreport = None):
        self.name = name
        self.index = index
        self.data = points
        self.section_averages = averages
        self.overallrep = overallreport
    def head(self):
        lines = []
        lines.append('<link class="include" rel="stylesheet" type="text/css" href="../../../Graphs/examples/../jquery.jqplot.min.css" />' + endl)
        #lines.append('<link rel="stylesheet" type="text/css" href="../../Graphs/examples/examples.min.css" />' + endl)
        lines.append('<link type="text/css" rel="stylesheet" href="../../../Graphs/examples/syntaxhighlighter/styles/shCoreDefault.min.css" />' + endl)
        lines.append('<link type="text/css" rel="stylesheet" href="../../../Graphs/examples/syntaxhighlighter/styles/shThemejqPlot.min.css" />' + endl)
        lines.append('<script class="include" type="text/javascript" src="../../../Graphs/jquery.min.js"></script>' + endl)
        return lines


    def html(self, percent=False, space = True, SIMPLE_REP_FLAG = False):
        lines = []
        if space:
            lines.append('<br>')
        lines.append('<div id="chart' + str(self.index) + '" style="height:300px; width:490px;"></div>' + endl)
        lines.append('<script class="code" type="text/javascript">' + endl)
        lines.append('$(document).ready(function(){' + endl)
        #if SIMPLE_REP_FLAG:
         #   lines.append("var labels = ['Class Average', 'Your Performance'];" + endl)
        lines.append('var line1 = ' + str(self.data) + ';' + endl)
        if SIMPLE_REP_FLAG :
            filename = class_directory('Elite') + DIR_SEP + "average.txt"
            with open(filename) as f:
                array = f.readlines()
                l = {}
                total = 0
                current_date = None
                for line in array:
                    line = line.strip()
                    if line == '':
                        continue
                    if 'TEST_DATE' in line:
                        current_date = line.split(' ')[1]
                    if 'WRITING:' in line:
                        total += int(line.split(' ')[1])
                        
                    if 'MATH:' in line:
                        total += int(line.split(' ')[1])
                        
                    if 'READING:' in line:
                        total += int(line.split(' ')[1])

                    if SECTION_SEP in line:
                        l[current_date] = total
                        total = 0
                #lines.append("var line2 = " + str(l) + ";" + endl)
            op= []
            for entry in self.data:
                new_entry = [entry[0], l[entry[0]]]
                op.append(new_entry)

            lines.append("var line2 = " + str(op) + ";" + endl)
            lines.append("var labels = ['Class Average', 'Your Performance'];" + endl)
            lines.append("var plot1 = $.jqplot('chart" + str(self.index) + "', [line1, line2], {" + endl)
        elif self.section_averages != None:
                lines.append("var labels = ['Your Performance', 'Class Average'];" + endl)
                lines.append("var line2 = " + str(self.section_averages) + ";" + endl)
                lines.append("var plot1 = $.jqplot('chart" + str(self.index) + "', [line1, line2], {" + endl)

        else:
            lines.append("var labels = ['Your Performance', 'Class Average'];" + endl)
            #lines.append("var line2 = " + str(self.section_averages) + ";" + endl)
            lines.append("var plot1 = $.jqplot('chart" + str(self.index) + "', [line1], {" + endl)
        lines.append("animate: true," + endl)
        lines.append("animateReplot:true," + endl)
        lines.append("title:'" + self.name + "'," + endl)
        lines.append('seriesDefaults: {' + endl)
        lines.append('showMarker:true,' + endl)
        lines.append('pointLabels: { show:false } ' + endl)
        lines.append('},' + endl)
        if SIMPLE_REP_FLAG or self.section_averages != None:

            lines.append("legend: {" + endl)
            lines.append("show: true," + endl)
            lines.append("renderer: $.jqplot.EnhancedLegendRenderer," + endl)
            lines.append("rendererOptions: {" + endl)
            lines.append("numberRows: 2" + endl)
            lines.append("}," + endl)
            lines.append("placement: 'insideGrid'," + endl)
            lines.append("labels: labels," + endl)
            lines.append("location: 'se'" + endl)
            lines.append("}," + endl)
        '''        
        if SIMPLE_REP_FLAG :
            lines.append("legend: {" + endl)
            lines.append("show: true," + endl)
            lines.append("renderer: $.jqplot.EnhancedLegendRenderer," + endl)
            lines.append("rendererOptions: {" + endl)
            lines.append("numberRows: 2" + endl)
            lines.append("}," + endl)
            lines.append("placement: 'insideGrid'," + endl)
            lines.append("labels: labels," + endl)
            lines.append("location: 'se'" + endl)
            lines.append("}," + endl)
        '''
        lines.append('highlighter:{ show: true, sizeAdjust: 7.5},' + endl)
        lines.append('axes:{' + endl)
        lines.append('xaxis:{' + 'label:' + "'Date of Test Taken'," + 'renderer:$.jqplot.DateAxisRenderer, tickInterval:' + "'" + '2 week' + "'}," + endl)
        if SIMPLE_REP_FLAG or self.overallrep == True:
            lines.append("yaxis:{" 'min:0, max:2400,'+ 'label:' + "'Score'," + 'labelRenderer: $.jqplot.CanvasAxisLabelRenderer,' + '}' + endl)
        elif self.section_averages != None:
            lines.append("yaxis:{" 'min:0, max:800,'+ 'label:' + "'Score'," + 'labelRenderer: $.jqplot.CanvasAxisLabelRenderer,' + '}' + endl)

        elif percent:
            lines.append("yaxis:{" + 'label:' + "'Percent Correct'," + 'labelRenderer: $.jqplot.CanvasAxisLabelRenderer,' + "tickOptions: {formatString: " +  '"' +'%' + "'d" + '%"' + '}}' + endl)    
        else:
            lines.append("yaxis:{" 'label:' + "'Score'," + 'labelRenderer: $.jqplot.CanvasAxisLabelRenderer,' + '}' + endl)
        lines.append('},' + endl)
        lines.append("cursor: { show: true, zoom: true, looseZoom: true, showTooltip: false }," + endl)
        lines.append("series:[{lineWidth:1, rendererOptions:{animation:{speed:4000}}}]," + endl)
        lines.append('});' + endl)
        lines.append('});' + endl)
        lines.append('</script>' + endl)
        return lines


    def body(self):
        lines = []
        lines.append('<script class="include" type="text/javascript" src="../../../Graphs/examples/../jquery.jqplot.min.js"></script>' + endl)
        lines.append('<script type="text/javascript" src="../../../Graphs/examples/syntaxhighlighter/scripts/shCore.min.js"></script>' + endl)
        lines.append('<script type="text/javascript" src="../../../Graphs/examples/syntaxhighlighter/scripts/shBrushJScript.min.js"></script>' + endl)
        lines.append('<script type="text/javascript" src="../../../Graphs/examples/syntaxhighlighter/scripts/shBrushXml.min.js"></script>' + endl)
        lines.append('<script class="include" language="javascript" type="text/javascript" src="../../../Graphs/examples/../plugins/jqplot.barRenderer.min.js"></script>' + endl)
        lines.append('<script class="include" language="javascript" type="text/javascript" src="../../../Graphs/examples/../plugins/jqplot.categoryAxisRenderer.min.js"></script>' + endl)
        lines.append('<script class="include" language="javascript" type="text/javascript" src="../../../Graphs/examples/../plugins/jqplot.pointLabels.min.js"></script>' + endl)
        lines.append('<script class="include" language="javascript" type="text/javascript" src="../../../Graphs/examples/../plugins/jqplot.dateAxisRenderer.min.js"></script>' + endl)
        lines.append('<script class="include" type="text/javascript" src="../../../Graphs/examples/../plugins/jqplot.canvasTextRenderer.min.js"></script>' + endl)
        lines.append('<script class="include" type="text/javascript" src="../../../Graphs/examples/../plugins/jqplot.canvasAxisLabelRenderer.min.js"></script>' + endl)
        lines.append('<script type="text/javascript" src="../../../Graphs/examples/../plugins/jqplot.highlighter.min.js"></script>' + endl)
        lines.append('<script type="text/javascript" src="../../../Graphs/examples/../plugins/jqplot.cursor.min.js"></script>' + endl)
        lines.append('<script type="text/javascript" src="../../../Graphs/examples/../plugins/jqplot.dateAxisRenderer.min.js"></script>' + endl)
        lines.append('<script type="text/javascript" src="../../../Graphs/examples/../plugins/jqplot.enhancedLegendRenderer.min.js"></script>' + endl)
        return lines


class C_Graph(object):

    def __init__(self, name, index, points, schval, schnm, schcol, schbgcol):
        self.name = name
        self.index = index
        self.data = points
        # canvas overlay vars
        self.schscore = schval
        self.schname = schnm 
        self.schcolr = schcol
        self.schgbcolr = schbgcol
    def head(self):
        lines = []
        lines.append('<link class="include" rel="stylesheet" type="text/css" href="../../../Graphs/examples/../jquery.jqplot.min.css" />' + endl)
        #lines.append('<link rel="stylesheet" type="text/css" href="../../Graphs/examples/examples.min.css" />' + endl)
        lines.append('<link type="text/css" rel="stylesheet" href="../../../Graphs/examples/syntaxhighlighter/styles/shCoreDefault.min.css" />' + endl)
        lines.append('<link type="text/css" rel="stylesheet" href="../../../Graphs/examples/syntaxhighlighter/styles/shThemejqPlot.min.css" />' + endl)
        lines.append('<script class="include" type="text/javascript" src="../../../Graphs/jquery.min.js"></script>' + endl)
        return lines


    def html(self, percent=False, space = True):
        lines = []
        if space:
            lines.append('<br>')
        lines.append('<div id="chart' + str(self.index) + '" style="height:300px; width:500px;"></div>' + endl)
        lines.append('<script class="code" type="text/javascript">' + endl)
        lines.append('$(document).ready(function(){' + endl)
        lines.append('var line1 = ' + str(self.data) + ';' + endl)
        lines.append("var plot1 = $.jqplot('chart" + str(self.index) + "', [line1], {" + endl)
        lines.append("animate: true," + endl)
        lines.append("animateReplot:true," + endl)
        lines.append("title:'" + self.name + "'," + endl)
        lines.append('seriesDefaults: {' + endl)
        lines.append('showMarker:true,' + endl)
        lines.append('pointLabels: { show:false } ' + endl)
        lines.append('},' + endl)
        lines.append('highlighter:{ show: true, sizeAdjust: 7.5 },' + endl)
        #lines.append("legend:{ show: true, location: e , placement: inside   },' " + endl)
        lines.append('axes:{' + endl)
        lines.append('xaxis:{min:0},' + endl)
        if percent:
            lines.append("yaxis:{" + 'label:' + "'Percent Correct'," + 'labelRenderer: $.jqplot.CanvasAxisLabelRenderer,' + "tickOptions: {formatString: " +  '"' +'%' + "'d" + '%"' + '}}' + endl)
        else:
            lines.append("yaxis:{" + 'label:' + "'Score'," + 'labelRenderer: $.jqplot.CanvasAxisLabelRenderer,' + '}' + endl)
        lines.append('},' + endl)
        lines.append("cursor: { show: true, zoom: true, looseZoom: true, showTooltip: false }," + endl)
        lines.append("series:[{lineWidth:1, rendererOptions:{animation:{speed:4000}}}]," + endl)
        # canvas overlay
        lines.append("canvasOverlay: { show: true, objects: [ {horizontalLine: { name: '" + str(self.schname) + "', y: '"  + str(self.schscore) +  "', showTooltip: true, tooltipFormatString:  " '"' + str(self.schscore) + '"'  ", lineWidth: 4 ,color: " "'" + str(self.schcolr)  + "'" "}} , {dashedHorizontalLine: { name: '" + str(self.schname) + "', y: '"  + str(self.schscore) + "'" ", lineWidth: 5 , dashPattern: [12,12],color: " "'" + str(self.schgbcolr) + "'" "}}]}"   + endl )
        lines.append('});' + endl)
        lines.append('});' + endl)
        lines.append('</script>' + endl)
        return lines


    def body(self):
        lines = []
        lines.append('<script class="include" type="text/javascript" src="../../../Graphs/examples/../jquery.jqplot.min.js"></script>' + endl)
        lines.append('<script type="text/javascript" src="../../../Graphs/examples/syntaxhighlighter/scripts/shCore.min.js"></script>' + endl)
        lines.append('<script type="text/javascript" src="../../../Graphs/examples/syntaxhighlighter/scripts/shBrushJScript.min.js"></script>' + endl)
        lines.append('<script type="text/javascript" src="../../../Graphs/examples/syntaxhighlighter/scripts/shBrushXml.min.js"></script>' + endl)
        lines.append('<script class="include" language="javascript" type="text/javascript" src="../../../Graphs/examples/../plugins/jqplot.barRenderer.min.js"></script>' + endl)
        lines.append('<script class="include" language="javascript" type="text/javascript" src="../../../Graphs/examples/../plugins/jqplot.categoryAxisRenderer.min.js"></script>' + endl)
        lines.append('<script class="include" language="javascript" type="text/javascript" src="../../../Graphs/examples/../plugins/jqplot.pointLabels.min.js"></script>' + endl)
        lines.append('<script class="include" language="javascript" type="text/javascript" src="../../../Graphs/examples/../plugins/jqplot.dateAxisRenderer.min.js"></script>' + endl)
        lines.append('<script class="include" type="text/javascript" src="../../../Graphs/examples/../plugins/jqplot.canvasTextRenderer.min.js"></script>' + endl)
        lines.append('<script class="include" type="text/javascript" src="../../../Graphs/examples/../plugins/jqplot.canvasAxisLabelRenderer.min.js"></script>' + endl)
        # Canvas overlay 
        lines.append('<script language="javascript" type="text/javascript" src="../../../Graphs/examples/../plugins/jqplot.canvasOverlay.min.js"></script>' + endl)
        # Highlighter
        lines.append('<script type="text/javascript" src="../../../Graphs/examples/../plugins/jqplot.highlighter.min.js"></script>' + endl)
        lines.append('<script type="text/javascript" src="../../../Graphs/examples/../plugins/jqplot.cursor.min.js"></script>')
        return lines

class College_Profile(object):

       
        def report(self, schoolname, overall, math, reading, writing, name, classname):
            schools = schoolname
            p_o = overall
            p_m  = math
            p_r = reading
            p_w = writing
            index = 0
            dirc = user_directory(name, classname)
            FILE = open(dirc + DIR_SEP + "college_profile" + ".html", "w")
            lines = []

            
      
            #HTML opener
            lines.append('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">' + endl)
            lines.append('<html xmlns="http://www.w3.org/1999/xhtml">' + endl)
            lines.append('<head>')
            lines.append('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />' + endl)
            lines.append('<link rel="stylesheet" type="text/css" href="../../../HTML/style.css" />' + endl)
            lines.append('<title>Advanced Score Report</title>' + endl)
            lines.append('</head>' + endl)
            lines.append('<body>' + endl)
            lines.append('<div id="page">' + endl)
            lines.append('<div id="header">' + endl)
            lines.append('<img src="../../../HTML/EliteLogo.png" width="35%" alt="Excelerate" />' + endl)
            lines.append('</div>' + endl)
            lines.append('</div>' + endl)
            lines.append('<div id="content">' + endl)
            lines.append('<div id="container">' + endl)
            lines.append('<div id="main">' + endl)
            lines.append('<div id="menu">' + endl)
            lines.append('<h2 style="text-align:center;">' + str(name) + '</h2>' + endl)
            lines.append('</div>' + endl)
            lines.append('<div id="text">' + endl)


            #Class Analysis
            lines.append(endl)
            lines.append("<h1> College Profile</h1>" + endl)
            lines.append("<head>")
            lines.append("<style>")
            lines.append("table,th,td{border:1px solid black;border-collapse:collapse;}th,td{padding:5px;}th{text-align:left;}")
            lines.append("</style>")
            lines.append("</head>")

            lines.append('<table style="width:500px">')
            lines.append('<tr><th>College</th><th>Percent Of Students Admitted With Your Overall Score</th><th>Percent Of Students Admitted With Your Math Score</th><th>Percent Of Students Admitted With Your Reading Score</th><th>Percent Of Students Admitted With Your Writing Score</th></tr>')

            index = 0
            for school in schools:
                lines.append('<tr>')
                lines.append('<td>' + school + '</td>')
                lines.append('<td>' + str(p_o[index]) + '%</td>')
                lines.append('<td>' + str(p_m[index]) + '%</td>')
                lines.append('<td>' + str(p_r[index]) + '%</td>')
                lines.append('<td>' + str(p_w[index]) + '%</td>')
                lines.append('</tr>')
                index += 1 
            lines.append('</table>')

            #Footer
            lines.append('<br>' + endl)
            lines.append('</div>' + endl)
            lines.append('</div>' + endl)
            lines.append('</div>' + endl)
            lines.append('<div class="clear"></div>' + endl)
            lines.append('<div id="footer">' + endl)
            #lines.append('<p><a>' + 'College Profile Report</a></p>' + endl)
            lines.append('<p><img src="../../../HTML/Mini Logo.png" width="8%" alt="Excelerate" /></p>' + endl)
            lines.append('</div>' + endl)
            lines.append('</div>' + endl)


            lines.append('</body>' + endl)
            lines.append('</html>' + endl)
            lines.append(endl)

            FILE.writelines(lines)
            FILE.close()



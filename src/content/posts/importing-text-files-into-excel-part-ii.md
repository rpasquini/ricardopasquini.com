---
title: "Importing text files into Excel Part II / Importar archivos de texto al Excel Parte II"
date: "2011-02-03"
slug: "importing-text-files-into-excel-part-ii"
lang: "es"
categories: ["Coding Notes", "Uncategorized"]
tags: ["Stata", "Tablas", "Tables", "VBA"]
excerpt: ""
draft: false
---

[español](http://rpasquini.wordpress.com/2011/02/03/importing-text-files-into-excel-part-ii/2/)
For those who find useful to transfer the output of their statistics and regressions to Excel, here is another macro that might be useful.
As in the last case, imagine that you are dealing with many tables of statistics and regressions that you have computed with Stata, and you will find useful to take them all to Excel. Such a thing might be useful for visualization, comparing statistics (robustness checks), formatting the tables for presentations or publications, elaborating further graphics, and so on.
Building on the macro presented in the previous post, this time I built another one to deal with importing multiple files simultaneously.
To see how it works, imagine, as an example, that you have 5 key variables that you are analysing and for each of them you have produced 4 tables (corresponding, for example to different estimation methods) and exported each respectively to a text file. That gives a total of 20 tables to be imported from Excel.
First, it might be useful to organize the text files information in a table in Excel as shown in the table below:
[![](/media/2011/02/multipletextfiles.jpg "multipletextfiles")](/media/2011/02/multipletextfiles.jpg)
Using the information in the previous table, the multipletextload macro will :
i. Generate a new sheet for each variable (one for each row in the reference table) andname the sheet with the name of the corresponding variable.
ii. Paste the contents of all the tables corresponding to a same variable (in columns) within a same sheet, one table next to the right to each other.
iii. In case the macro do not find a specific file (might be the case that you did not want to apply a method for a given variable), will skip it and jump to the next file to import.
The macro uses the macro "Textload" that I have posted in the previous post, so you will have to generate the former one in order to run this one.
In order to run it, just select the contents of the table (in my example first select cells A2:E6 and then run the macro)
[sourcecode language="vb" firstline="1" highlight="16,22,24,29,35" padlinenumbers="false"]
Sub multipletextload()
Dim rgFiles As Range
Dim i As Long, j As Long
Dim sName As String
Dim fName As String
Dim strWork As String
'Dim LastRow As Long
Dim LastCol As Long
strWork = ThisWorkbook.Name
Set rgFiles = Selection
'Set rgFiles = Range("B2:F4")
For i = 1 To rgFiles.Rows.Count
'Row i Column 1 has the name of the variable. generate and name new sheet
sName = rgFiles.Cells(i, 1).Value
'sName = ActiveCell.Value
Sheets.Add(After:=ActiveSheet).Name = sName
'Add After:=ActiveSheet,
For j = 2 To rgFiles.Columns.Count
' Row i Columns 2 onwards have the names of the files to import
fName = rgFiles.Cells(i, j).Value
'If there is no name in the cell, not do anything
If fName = "" Then
Else
If j = 2 Then
' Only the file in Column 2 will be imported into cell (1,1)
Worksheets(sName).Cells(1, 1).Activate
ActiveCell.FormulaR1C1 = fName
Application.Run "Textload"
' Application.Run "'reg results\_vtest.xlsm'!Textload"
Else
' The remaining will be imported to cell location (1,LastCol)
Worksheets(sName).Cells(1, 1).Activate
Set rgLast = Worksheets(sName).Range("A1").SpecialCells(xlCellTypeLastCell)
'LastRow = rgLast.Row
LastCol = rgLast.Column
Worksheets(sName).Range("A1").Cells(1, LastCol).FormulaR1C1 = fName
Worksheets(sName).Range("A1").Cells(1, LastCol).Activate
Application.Run "Textload"
End If
End If
Next j
Next i
End Sub
[/sourcecode]
Para aquellos que encuentran útil importar sus cuadros de estadísticas y regresiones al Excel, aquí va otra macro que puede ser útil.
Al igual que en el último caso, imaginen que están trabajando con muchas tablas de estadísticas y o de regresiones que se ha calculado con Stata, y querríamos importar todas al Excel. Tal cosa podría ser útil para la visualización, comparación de las estadísticas (pruebas de robustez), el formato de las tablas para las presentaciones o publicaciones, elaboración de gráficos , o cuestiones por el estilo.
Sobre la base de la macro presentada en el post anterior, esta vez construi otra para importar varios archivos simultáneamente.
Supongamos que nuestro análisis se organiza alrededor de 5 variables y para cada una de ellas contamos con 4 tablas de estadisticas o regresiones (correspondientes, por ejemplo, a diferentes métodos de estimación). Todas estas tablas se han computado en STATA y exportado a archivos de texto. Eso da un total de 20 tablas para ser importadas al Excel.
En primer lugar, podría ser útil para organizar los nombres de los archivos de texto en una tabla en Excel como se muestra en el cuadro siguiente:
[![](/media/2011/02/multipletextfiles.jpg "multipletextfiles")](/media/2011/02/multipletextfiles.jpg)
Utilizando la información en la tabla anterior, lo que hara esta macro (multipletextload) es lo siguiente:
i. Generar una nueva hoja para cada variable (uno para cada fila de la tabla de referencia) y llamar a la hoja con el nombre de la variable correspondiente.
ii. Peguar el contenido de todos los cuadros correspondientes a una misma variable (en columnas) dentro de una misma hoja, una tabla a la derecha inmediatamente la una de la otra.
iii. En el caso de que la macro no encuentre el archivo especificado, saltara al siguiente archivo que desea importar.
La macro utiliza la macro "Textload" que he publique en el post anterior, por lo que tendrá que generar la anterior con el para ejecutar esta.
Para ejecutarla, sólo tienes que seleccionar el contenido de la tabla (en mi ejemplo seleccione las celdas A2:E6 y, a continuación, ejecutar la macro)
[sourcecode language="vb" firstline="1" highlight="16,22,24,29,35" padlinenumbers="false"]
Sub multipletextload()
Dim rgFiles As Range
Dim i As Long, j As Long
Dim sName As String
Dim fName As String
Dim strWork As String
'Dim LastRow As Long
Dim LastCol As Long
strWork = ThisWorkbook.Name
Set rgFiles = Selection
'Set rgFiles = Range("B2:F4")
For i = 1 To rgFiles.Rows.Count
'Row i Column 1 has the name of the variable. generate and name new sheet
sName = rgFiles.Cells(i, 1).Value
'sName = ActiveCell.Value
Sheets.Add(After:=ActiveSheet).Name = sName
'Add After:=ActiveSheet,
For j = 2 To rgFiles.Columns.Count
' Row i Columns 2 onwards have the names of the files to import
fName = rgFiles.Cells(i, j).Value
'If there is no name in the cell, not do anything
If fName = "" Then
Else
If j = 2 Then
' Only the file in Column 2 will be imported into cell (1,1)
Worksheets(sName).Cells(1, 1).Activate
ActiveCell.FormulaR1C1 = fName
Application.Run "Textload"
' Application.Run "'reg results\_vtest.xlsm'!Textload"
Else
' The remaining will be imported to cell location (1,LastCol)
Worksheets(sName).Cells(1, 1).Activate
Set rgLast = Worksheets(sName).Range("A1").SpecialCells(xlCellTypeLastCell)
'LastRow = rgLast.Row
LastCol = rgLast.Column
Worksheets(sName).Range("A1").Cells(1, LastCol).FormulaR1C1 = fName
Worksheets(sName).Range("A1").Cells(1, LastCol).Activate
Application.Run "Textload"
End If
End If
Next j
Next i
End Sub
[/sourcecode]

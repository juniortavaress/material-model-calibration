class ExcelUtils():
    @staticmethod
    def create_formats(workbook):
        """
        Creates and returns predefined cell formats for an Excel workbook.

        Args:
            workbook (xlsxwriter.workbook.Workbook): The workbook where formats will be applied.

        Returns:
            tuple: A tuple containing gray-filled and centered formats.
        """
        gray_fill_format = workbook.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter', 'bg_color': '#D9D9D9', 'border': 1})
        centered_format = workbook.add_format({'align': 'center', 'valign': 'vcenter'})  # Zentrale Formatierung
        return gray_fill_format, centered_format


    @staticmethod
    def format_statistics_sheet_xlsxwriter(worksheet, workbook, temperature_threshold, start_percent, end_percent):
        """
        Formats the statistics worksheet with headers and specific styles.

        Args:
            worksheet (xlsxwriter.worksheet.Worksheet): The worksheet to be formatted.
            workbook (xlsxwriter.workbook.Workbook): The workbook containing the worksheet.
            temperature_threshold (float): The temperature threshold for penetration depth evaluation.
            start_percent (float): The starting percentage for the cutting force range.
            end_percent (float): The ending percentage for the cutting force range.
        """
        gray_fill_format, centered_format = ExcelUtils.create_formats(workbook)

        # Merging cells for descriptive headers
        try:
            worksheet.merge_range('B1:E1', f"Normal Cutting Force FcN in the range of {start_percent*100:.0f}-{end_percent*100:.0f} % [N]", gray_fill_format)
            worksheet.merge_range('F1:I1', f"Cutting Force Fc in the range of {start_percent*100:.0f}-{end_percent*100:.0f} % [N]", gray_fill_format)
            worksheet.merge_range('J1:K1', 'Temperature Evaluation at the Last Frame', gray_fill_format)
            worksheet.merge_range('L1:M1', 'Temperature Evaluation at Frame with Tmax at 1st Node', gray_fill_format)
        except:
            pass
        
        # Define statistics headers (minimum, maximum, mean, standard deviation, etc.)
        statistics_headers = [
            "Filename", "Minimum", "Maximum", "Mean", "Standard Deviation",
            "Minimum", "Maximum", "Mean", "Standard Deviation",
            "Maximum Temperature [°C]", f"Penetration Depth for Temperature < {temperature_threshold}°C [µm]",
            "Maximum Temperature [°C]", f"Penetration Depth for Temperature < {temperature_threshold}°C [µm]"
        ]

        # Write the headers to the worksheet
        for col_num, header in enumerate(statistics_headers):
            worksheet.write(1, col_num, header, gray_fill_format)

        # Set column widths and apply centered formatting
        column_widths = [42, 15, 15, 15, 20, 15, 15, 15, 20, 27, 45, 27, 45]
        for col_num, width in enumerate(column_widths):
            worksheet.set_column(col_num, col_num, width, centered_format)
        worksheet.set_zoom(80)


    @staticmethod
    def format_excel_sheet(worksheet, workbook):
        """    
        Formats the Excel worksheet, including headers and column widths.

        Args:
            worksheet (xlsxwriter.worksheet.Worksheet): The worksheet to be formatted.
            workbook (xlsxwriter.workbook.Workbook): The workbook containing the worksheet.
        """
        gray_fill_format, centered_format = ExcelUtils.create_formats(workbook)

        # Writing the headers for the main sheet
        headers = [
            ('A1', 'Time [ms]'),
            ('B1', 'Cutting Force Fc [N]'),
            ('C1', 'Normal Cutting Force FcN [N]'),
            ('E1', 'Penetration Depth [µm]'),
            ('F1', 'Temperature at Last Frame [°C]'),
            ('G1', 'Maximum Temperature [°C]'),
            ('I1', 'Time [ms]'),
            ('J1', 'Temperature at 1st Node [°C]')
        ]
        
        for cell, header in headers:
            worksheet.write(cell, header, gray_fill_format)

        # Setting column widths 
        column_widths = [10, 20, 30, 20, 30, 33, 25, 20, 10, 27]
        for col_num, width in enumerate(column_widths):
            worksheet.set_column(col_num, col_num, width, centered_format)
        worksheet.set_zoom(90)


    @staticmethod
    def add_forces_graps_to_excel(writer, sheet_name, df):
        """
        Adds force-related graphs to an Excel worksheet.

        Args:
            writer (pandas.ExcelWriter): Excel writer object.
            sheet_name (str): Name of the worksheet to add charts.
            df (pd.DataFrame): DataFrame containing the data for the charts.
        """
        workbook = writer.book
        worksheet = writer.sheets[sheet_name]

        # Apply basic formatting to the worksheet
        ExcelUtils.format_excel_sheet(worksheet, workbook)

        # Add chart 1: Force components over time
        chart1 = workbook.add_chart({'type': 'scatter', 'subtype': 'straight_with_markers'})

        # Series for Cutting Force Fc [N]
        categories1 = [sheet_name, 1, 0, len(df), 0]  # Time
        values1 = [sheet_name, 1, 1, len(df), 1]      # Cutting Force Fc [N]
        chart1.add_series({'name': 'Cutting Force Fc', 'categories': categories1, 'values': values1, 'marker': {'type': 'none'}, 'line': {'width': 1.5}})

        # Series for Normal Cutting Force FcN [N]
        values2 = [sheet_name, 1, 2, len(df), 2]  # Normal Cutting Force FcN [N]
        chart1.add_series({'name': 'Normal Cutting Force FcN', 'categories': categories1, 'values': values2, 'marker': {'type': 'none'}, 'line': {'width': 1.5}})

        # Configure chart title and axes
        chart1.set_title({'name': sheet_name, 'name_font': {'size': 14}})
        chart1.set_x_axis({'name': 'Time t [ms]', 'name_font': {'size': 11}, 'num_font': {'size': 11}})
        chart1.set_y_axis({'name': 'Force Component Fi [N]', 'name_font': {'size': 11}, 'num_font': {'size': 11}})
        chart1.set_legend({'position': 'bottom', 'font': {'size': 11}})
        worksheet.insert_chart('L2', chart1)


    @staticmethod
    def add_temp_graps_to_excel(writer, sheet_name, df):
        """
        Adds temperature-related graphs to an Excel worksheet.

        Args:
            writer (pandas.ExcelWriter): Excel writer object.
            sheet_name (str): Name of the worksheet to add charts.
            df (pd.DataFrame): DataFrame containing the data for the charts.
        """
        workbook = writer.book
        worksheet = writer.sheets[sheet_name]

        # Chart 2: Temperature vs. Penetration Depth
        chart2 = workbook.add_chart({'type': 'scatter', 'subtype': 'straight_with_markers'})
        categories2 = [sheet_name, 1, 4, len(df), 4]  
        values3 = [sheet_name, 1, 5, len(df), 5]      
        chart2.add_series({
            'name': 'Temperatur beim letzten Frame',
            'categories': categories2,
            'values': values3,
            'marker': {'type': 'none'},
            'line': {'width': 1.5},
        })
        
        # Series for Maximum Temperature
        values4 = [sheet_name, 1, 6, len(df), 6]    
        chart2.add_series({
            'name': 'Maximaltemperatur',
            'categories': categories2,
            'values': values4,
            'marker': {'type': 'none'},
            'line': {'width': 1.5},
        })

        chart2.set_title({'name': sheet_name, 'name_font': {'size': 14}})
        chart2.set_x_axis({'name': 'Eindringtiefe [µm]', 'name_font': {'size': 11}, 'num_font': {'size': 11}})
        chart2.set_y_axis({'name': 'Temperatur T [°C]', 'name_font': {'size': 11}, 'num_font': {'size': 11}})
        chart2.set_legend({'position': 'bottom', 'font': {'size': 11}})
        worksheet.insert_chart('L20', chart2)

        # Chart 3: Temperature at Node vs. Time
        chart3 = workbook.add_chart({'type': 'scatter', 'subtype': 'straight_with_markers'})
        categories3 = [sheet_name, 1, 8, len(df), 8]  
        values5 = [sheet_name, 1, 9, len(df), 9]      
        chart3.add_series({
            'name': 'Temperatur am 1. Knoten',
            'categories': categories3,
            'values': values5,
            'marker': {'type': 'none'},
            'line': {'width': 1.5},
        })
        
        chart3.set_title({'name': sheet_name, 'name_font': {'size': 14}})
        chart3.set_x_axis({'name': 'Zeit t [ms]', 'name_font': {'size': 11}, 'num_font': {'size': 11}})
        chart3.set_y_axis({'name': 'Temperatur am 1. Knoten [°C]', 'name_font': {'size': 11}, 'num_font': {'size': 11}})
        chart3.set_legend({'none': True})
        worksheet.insert_chart('L37', chart3)
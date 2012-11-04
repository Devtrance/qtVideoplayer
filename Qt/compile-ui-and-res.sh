#!/usr/bin/env bash
#
#   compile-ui-and-res.sh
#
#        This program is free software: you can redistribute it and/or modify
#        it under the terms of the GNU General Public License as published by
#        the Free Software Foundation, either version 3 of the License, or
#        (at your option) any later version.
#
#        This program is distributed in the hope that it will be useful,
#        but WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#        GNU General Public License for more details.
#
#        You should have received a copy of the GNU General Public License
#        along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#              - Author:    Devnix
#              - Website:   http://devtrance.com
#              - Contact:   devnix.code@gmail.com
#
# This bash script compiles all the resources and ui files founded on this directory with PySide.
# It follows the next format, you can change the destitation directory for your project:
#     FOR UI FILES:         pyside-uic $DIR/example.ui > $DESTINATION/example_ui.py
#     FOR QRC FILES:      pyside-rcc $DIR/example.qrc -o $DESTINATION/example_rc.py

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"     # Gets the actual directory
DESTINATION="$( cd "$DIR"/../src/ui && pwd)"                      # Gets the destination directory

ERROR="false"

function compile_ui { 
    for ui_file in $DIR/*.ui
    do
        filename=$(basename "$ui_file")
        extension="${filename##*.}"
        filename="${filename%.*}"                       # This gets the file name without extension
        
        ui_destination=$DESTINATION"/"$filename"_ui.py"
        
        echo "Compiling from: $ui_file"
        echo "To: $ui_destination"
        
        echo -ne " - "
        
        pyside-uic $ui_file > $ui_destination
        
        if [ $? -eq 0 ]; then
            echo "Success!"
         else
            ERROR="true"
         fi
         echo ""
    done
}

function compile_qrc { 
    for qrc_file in $DIR/*.qrc
    do
        filename=$(basename "$qrc_file")
        extension="${filename##*.}"
        filename="${filename%.*}"                       # This gets the file name without extension
        
        qrc_destination=$DESTINATION"/"$filename"_rc.py"
        
        echo "Compiling from: $qrc_file"
        echo "To: $qrc_destination"
        
        echo -ne " - "
        
        pyside-rcc $qrc_file -o $qrc_destination
        
        if [ $? -eq 0 ]; then
            echo "Success!"
         else
            ERROR="true"
         fi
         echo ""
    done
}

# MAIN CODE

echo ""

compile_ui
compile_qrc

if [ $ERROR == "true" ]; then
    echo -e " === WARNING: Some files couldn't be compiled ===\n"
fi

exit

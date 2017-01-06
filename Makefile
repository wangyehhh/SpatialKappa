# Download 
# http://www.antlr.org/share/1169924912745/antlr3-task.zip
# Unpack
# Put ant-antlr3.jar in ~/.ant/lib
# OR sudo apt-get install antlr3

# N.B.: The CLASSPATH has to have both parts and has to be aboslute
CLASSPATH=$(realpath .)/src/lib/antlr-3.2.jar:$(realpath .)/ant-antlr3.jar 

all: 
	cd build && ant
	cd build && CLASSPATH=$(CLASSPATH) ant compile-all
	cd build && ant -f buildSpatialKappa.xml

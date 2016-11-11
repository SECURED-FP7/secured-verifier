CC		:= cc 
CFLAGS		:= -fPIC -Werror
LDFLAGS		:= -s
OBJ		:= filevercmp.o filevercmp_deb.o filevercmp_java.o filevercmp_java_deb.o

%.o : %.c
	 $(CC) $(CFLAGS) -c $< -I $(JAVAHEADERS) -I $(JAVAHEADERS)/linux

libfilevercmp.so: $(OBJ)
	 $(CC) $(LDFLAGS) -shared -Wl,-soname,$@ -o $@ $(OBJ) -lrpm

rassandra.jar:
	javac -cp $(CASSANDRACLASSPATH) torsec/ra/cassandra/db/PackagesVersionType.java torsec/ra/cassandra/db/PackagesVersionTypeDEB.java 
	javah -jni -classpath $(CASSANDRACLASSPATH):. torsec.ra.cassandra.db.PackagesVersionType
	javah -jni -classpath $(CASSANDRACLASSPATH):. torsec.ra.cassandra.db.PackagesVersionTypeDEB
	jar cf rassandra.jar torsec

clean:
	rm -Rf *.o libfilevercmp.so rassandra.jar
	rm -Rf torsec/ra/cassandra/db/*.class
	rm -Rf torsec_ra_cassandra_db_PackagesVersionType*.h 

all:	rassandra.jar libfilevercmp.so

install:
	install -m 744 libfilevercmp.so $(DESTDIR)$(LIBDIR)
	install -m 644 rassandra.jar ${DESTDIR}$(CASSANDRADIR)/lib

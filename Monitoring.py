import psutil
import shutil
import logging

RAM = "90 %"
RAMAuslastung = ('RAM % used:', psutil.virtual_memory()[2])
RAMAuslastung_str = str(RAMAuslastung)
Prozessorauslastung = psutil.cpu_percent()
Arbeitsspeicherauslastung = psutil.virtual_memory()
Total, Used, Free = shutil.disk_usage("/")

#Dies sind Anhaltspunkte zum Verständnis und zum dauerhaften Monitoren. Die Ausgabe ist beabsichtigt.
print("CPU % used:", psutil.cpu_percent())
print("RAM % used:", psutil.virtual_memory()[2])
print("Total Disk Space: %d GiB" % (Total // (2**30)))
print("Used Disk Space: %d GiB" % (Used // (2**30)))
print("Free Disk Space: %d GiB" % (Free // (2**30)))

#An dieser Stelle wird die Log-Datei erstellt und beschrieben
logging.basicConfig(filename='Monitoring Log',level=logging.DEBUG)
logging.debug("CPU % used:", psutil.cpu_percent())
logging.info("RAM % used:", psutil.virtual_memory()[2])
logging.info("Total Disk Space: %d GiB" % (Total // (2**30)))
logging.info("Used Disk Space: %d GiB" % (Used // (2**30)))
logging.info("Free Disk Space: %d GiB" % (Free // (2**30)))

#Bei 90%iger Auslastung des Arbeitsspeichers wird eine Warnung im Log verzeichnet.
if RAM < RAMAuslastung_str:
    logging.info(print("Kritische RAM-Auslastung"))

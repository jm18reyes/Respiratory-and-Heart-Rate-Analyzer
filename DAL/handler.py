import sqlite3
from datetime import datetime
from nltk import flatten


class DataHandler(object):
	def __init__(self, db_file):
		self.dh = sqlite3.connect(db_file)
		self.c = self.dh.cursor()

		

	def initializePatient(self,p_id):
		self.name = "Edit Name"
		self.c.execute("INSERT INTO Patient (patient_id,name) VALUES (?,?)",(p_id,self.name))
		self.dh.commit()

		

	def initializePatientBackup(self,p_id):
		self.name = "Edit Name"
		self.c.execute("INSERT INTO Patient_backup (patient_id,name) VALUES (?,?)",(p_id,self.name))
		self.dh.commit()

	def initializeResult(self,p_id):
		self.breath = "Normal"
		self.heart = "Normal"
		self.c.execute("INSERT INTO Result (patient_id,breath_diagnosis,heart_diagnosis) VALUES (?,?,?)",(p_id,self.breath,self.heart))
		self.dh.commit()

	def initializeResultBackup(self,p_id):
		self.breath = "Normal"
		self.heart = "Normal"
		
		self.c.execute("INSERT INTO Result_backup (patient_id,breath_diagnosis,heart_diagnosis) VALUES (?,?,?)",(p_id,self.breath,self.heart))
		self.dh.commit()

	def insertData(self,p_id,breathVal,heartVal,minuteVal):
		
		self.c.execute("INSERT INTO Data (patient_id,breath,heartrate,minute) VALUES (?,?,?,?)",(p_id,breathVal,heartVal,minuteVal))
		self.dh.commit()

	def getLowRespiValues(self):
		self.c.execute("SELECT lowRespi_min,lowRespi_max FROM abnormality")
		results = flatten(self.c.fetchall())
		return results

	def getHighRespiValues(self):
		self.c.execute("SELECT highRespi_min,highRespi_max FROM abnormality")
		results = flatten(self.c.fetchall())
		return results

	def getLowHeartValues(self):
		self.c.execute("SELECT lowHeart_min,lowHeart_max FROM abnormality")
		results = flatten(self.c.fetchall())
		return results

	def getHighHeartValues(self):
		self.c.execute("SELECT highHeart_min,highHeart_max FROM abnormality")
		results = flatten(self.c.fetchall())
		return results

	def getLatestID(self):
		self.c.execute("SELECT MAX(patient_id) FROM Patient ")
		id, = self.c.fetchone()
		print(id)
		return id

	def getLatestIDFromBackup(self):
		self.c.execute("SELECT MAX(patient_id) FROM Patient_backup ")
		id, = self.c.fetchone()
		print(id)
		return id

	def getPatientIDList(self):
		self.c.execute("SELECT patient_id FROM Patient")
		results = flatten(self.c.fetchall())
		return results

	def getPatientBackupIDList(self):
		self.c.execute("SELECT patient_id FROM Patient_backup")
		results = flatten(self.c.fetchall())
		return results

	def getDataCount(self):
		self.c.execute("SELECT patient_id FROM Data")
		results = len(flatten(self.c.fetchall()))
		return results

	def getPatientINFO(self,p_id):
		self.c.execute("SELECT name,classification,age,height,weight FROM Patient WHERE patient_id=?",(p_id,))
		results = flatten(self.c.fetchall())
		return results

	def getBreathList(self,p_id):
		self.c.execute("SELECT breath FROM Data WHERE patient_id=?",(p_id,))
		results = flatten(self.c.fetchall())
		return results

	def getHeartRateList(self,p_id):
		self.c.execute("SELECT heartrate FROM Data WHERE patient_id=?",(p_id,))
		results = flatten(self.c.fetchall())
		return results

	def getMinuteList(self,p_id):
		self.c.execute("SELECT minute FROM Data WHERE patient_id=?",(p_id,))
		results = flatten(self.c.fetchall())
		return results

	def getBreathAve(self,p_id):
		self.c.execute("SELECT breath_average FROM Result WHERE patient_id=?",(p_id,))
		result, = self.c.fetchone()
		return result

	def getHeartrateAve(self,p_id):
		self.c.execute("SELECT heartrate_average FROM Result WHERE patient_id=?",(p_id,))
		result, = self.c.fetchone()
		return result

	def getBreathDiagnosis(self,p_id):
		self.c.execute("SELECT breath_diagnosis FROM Result WHERE patient_id=?",(p_id,))
		result, = self.c.fetchone()
		return result

	def getHeartDiagnosis(self,p_id):
		self.c.execute("SELECT heart_diagnosis FROM Result WHERE patient_id=?",(p_id,))
		result, = self.c.fetchone()
		return result

	def editPatientName(self,p_id,patientName):
		self.c.execute("UPDATE Patient SET name=? WHERE patient_id=?",(patientName,p_id))
		self.dh.commit()

		self.c.execute("UPDATE Patient_backup SET name=? WHERE patient_id=?",(patientName,p_id))
		self.dh.commit()

	def editPatientAge(self,p_id,patientAge):
		self.c.execute("UPDATE Patient SET age=? WHERE patient_id=?",(patientAge,p_id))
		self.dh.commit()

		self.c.execute("UPDATE Patient_backup SET age=? WHERE patient_id=?",(patientAge,p_id))
		self.dh.commit()

	def editPatientClass(self,p_id,patientClass):
		self.c.execute("UPDATE Patient SET classification=? WHERE patient_id=?",(patientClass,p_id))
		self.dh.commit()

		self.c.execute("UPDATE Patient_backup SET classification=? WHERE patient_id=?",(patientClass,p_id))
		self.dh.commit()

	def editPatientHeight(self,p_id,patientHeight):
		self.c.execute("UPDATE Patient SET height=? WHERE patient_id=?",(patientHeight,p_id))
		self.dh.commit()

		self.c.execute("UPDATE Patient_backup SET height=? WHERE patient_id=?",(patientHeight,p_id))
		self.dh.commit()

	def editPatientWeight(self,p_id,patientWeight):
		self.c.execute("UPDATE Patient SET weight=? WHERE patient_id=?",(patientWeight,p_id))
		self.dh.commit()

		self.c.execute("UPDATE Patient_backup SET weight=? WHERE patient_id=?",(patientWeight,p_id))
		self.dh.commit()

	def updateBreathDiagnosis(self,p_id,breathDiag):
		self.c.execute("UPDATE Result SET breath_diagnosis=? WHERE patient_id=?",(breathDiag,p_id))
		self.dh.commit()

		self.c.execute("UPDATE Result_backup SET breath_diagnosis=? WHERE patient_id=?",(breathDiag,p_id))
		self.dh.commit()

	def updateHeartDiagnosis(self,p_id,heartDiag):
		self.c.execute("UPDATE Result SET heart_diagnosis=? WHERE patient_id=?",(heartDiag,p_id))
		self.dh.commit()

		self.c.execute("UPDATE Result_backup SET heart_diagnosis=? WHERE patient_id=?",(heartDiag,p_id))
		self.dh.commit()

	def updateRangeForRespi(self,min_lowRespi,max_lowRespi,min_highRespi,max_highRespi):
		
		self.c.execute("UPDATE abnormality SET lowRespi_min=?,lowRespi_max=?,highRespi_min=?,highRespi_max=?",(min_lowRespi,max_lowRespi,min_highRespi,max_highRespi))
		self.dh.commit()

	def updateRangeForHeart(self,min_lowHeart,max_lowHeart,min_highHeart,max_highHeart):
		self.c.execute("UPDATE abnormality SET lowHeart_min=?,lowHeart_max=?,highHeart_min=?,highHeart_max=?",(min_lowHeart,max_lowHeart,min_highHeart,max_highHeart))
		self.dh.commit()

	def updateAverage(self,p_id,breathAve,heartAve):
		self.c.execute("UPDATE Result SET breath_average=?,heartrate_average=? WHERE patient_id=?",(breathAve,heartAve,p_id))
		self.dh.commit()

		self.c.execute("UPDATE Result_backup SET breath_average=?,heartrate_average=? WHERE patient_id=?",(breathAve,heartAve,p_id))
		self.dh.commit()

	def resetDatabase(self):
		self.c.execute("DELETE FROM Patient")
		self.dh.commit()

		self.c.execute("DELETE FROM Patient_backup")
		self.dh.commit()

		self.c.execute("DELETE FROM Data")
		self.dh.commit()

		self.c.execute("DELETE FROM Result")
		self.dh.commit()

		self.c.execute("DELETE FROM Result_backup")
		self.dh.commit()

	def safeClean(self):
		self.c.execute("DELETE FROM Data")
		self.dh.commit()

		self.c.execute("DELETE FROM Patient")
		self.dh.commit()

		self.c.execute("DELETE FROM Result")
		self.dh.commit()

	def prepareBackup(self):

		self.c.execute("UPDATE Patient_backup SET name=(SELECT Patient.name FROM Patient WHERE Patient_backup.patient_id = Patient.patient_id)")
		self.dh.commit()

		self.c.execute("UPDATE Patient_backup SET classification=(SELECT Patient.classification FROM Patient WHERE Patient_backup.patient_id = Patient.patient_id)")
		self.dh.commit()

		self.c.execute("UPDATE Patient_backup SET age=(SELECT Patient.age FROM Patient WHERE Patient_backup.patient_id = Patient.patient_id)")
		self.dh.commit()

		self.c.execute("UPDATE Patient_backup SET height=(SELECT Patient.height FROM Patient WHERE Patient_backup.patient_id = Patient.patient_id)")
		self.dh.commit()

		self.c.execute("UPDATE Patient_backup SET weight=(SELECT Patient.weight FROM Patient WHERE Patient_backup.patient_id = Patient.patient_id)")
		self.dh.commit()

	def restoreFromBackup(self):
		self.c.execute("UPDATE Patient SET name=(SELECT Patient_backup.name FROM Patient_backup WHERE Patient.patient_id = Patient_backup.patient_id)")
		self.dh.commit()

		self.c.execute("UPDATE Patient SET classification=(SELECT Patient_backup.classification FROM Patient_backup WHERE Patient.patient_id = Patient_backup.patient_id)")
		self.dh.commit()

		self.c.execute("UPDATE Patient SET age=(SELECT Patient_backup.age FROM Patient_backup WHERE Patient.patient_id = Patient_backup.patient_id)")
		self.dh.commit()

		self.c.execute("UPDATE Patient SET height=(SELECT Patient_backup.height FROM Patient_backup WHERE Patient.patient_id = Patient_backup.patient_id)")
		self.dh.commit()

		self.c.execute("UPDATE Patient SET weight=(SELECT Patient_backup.weight FROM Patient_backup WHERE Patient.patient_id = Patient_backup.patient_id)")
		self.dh.commit()


dh = DataHandler('../patient.db')

lowRespi = dh.getLowRespiValues()
highRespi = dh.getHighRespiValues()
lowHeart = dh.getLowHeartValues()
highHeart = dh.getHighHeartValues()

print(lowRespi)
print(highRespi)
print(lowHeart)
print(highHeart)


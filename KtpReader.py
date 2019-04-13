import cv2
import numpy
import re
from matplotlib import pyplot
import pytesseract

class KtpReader(object):

    result = {}

    def _readImage(self, path):

        image = cv2.imread(path)
        image = cv2.cvtColor(image, 6)

        kernel = numpy.ones((1, 1), numpy.uint8)

        result = pytesseract.image_to_string(image)

        return result

    def _getData(self, text):
        tok = ""
        data = {}
        isValue = 0
        text = text.rstrip()
        needle = ["NIK", "Nama", "Tempat/Tgl Lahir", "Jenis Kelamin", "Alamat", "RT/RW", "Kel/Desa", "Kecamatan", "Agama", "Status Perkawinan", "Pekerjaan", "Kewarganegaraan"]
        
        text = text.split("\n")
        for x in text:
            for i in needle:
                if re.match(".*" + i, x) != None:
                    value = x.split(i)[-1]
                    if i == "Jenis Kelamin":
                        value = value.split("Gol. Darah")
                        data["Gol. Darah"] = re.sub("[^a-zA-Z0-9 \\ \/]", "", value[-1])
                        data[i] = re.sub("[^a-zA-Z0-9 \\ \/]", "", value[0])
                    else:
                        data[i] = re.sub("[^a-zA-Z0-9 \\ \/]", "", value)
        for x in data:
            tok = ""
            values = data[x].split(" ")
            isStart = 0
            isKw = 0
            for i in values:
                if i != "":
                    if tok == "":
                        tok += i
                    elif x == "Kewarganegaraan":
                        pass
                    else:
                        tok += " " + i
            self.result[x] = tok

    def scan(self, image):
        data = self._readImage(image)
        self._getData(data)
        
        return len(self.result) == 13

    def get(self, key):
        
        if key in self.result:
            return self.result[key]
        else:
            return "data tidak ditemukan"
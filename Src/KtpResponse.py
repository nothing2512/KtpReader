class KtpResponse(object):

    Nik = ""
    Name = ""
    Dob = ""
    Gender = ""
    Address = ""
    Kelurahan = ""
    RtRw = ""
    Kecamatan = ""
    Religiion = ""
    Married = ""
    Work = ""
    Nationally = ""

    def __init__(self, data):
        self.Nik = data["NIK"]
        self.Name = data["Nama"]
        # self.Dob = data["Tempat/Tgl Lahir"]
        self.Gender = data["Jenis Kelamin"]
        self.Address = data["Alamat"]
        self.Kelurahan = data["Kel/Desa"]
        self.RtRw = data["RT/RW"]
        self.Kecamatan = data["Kecamatan"]
        self.Religiion = data["Agama"]
        self.Married = data["Status Perkawinan"]
        self.Work = data["Pekerjaan"]
        self.Nationally = data["Kewarganegaraan"]
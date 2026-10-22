
import tkinter as tk
from tkinter import ttk, messagebox
import re

# Indian states and union territories
states_districts = {
    "Andhra Pradesh": [
        "Alluri Sitharama Raju", "Anakapalli", "Anantapur",
        "Bapatla", "Chittoor", "East Godavari", "Eluru",
        "Guntur", "Kadapa", "Kakinada", "Krishna", "Kurnool",
        "Nandyal", "Nellore", "Palnadu", "Prakasam",
        "Srikakulam", "Tirupati", "Visakhapatnam", "Vizianagaram",
        "West Godavari"
    ],
    "Arunachal Pradesh": [
        "Anjaw", "Changlang", "Dibang Valley", "East Kameng",
        "East Siang", "Itanagar Capital Region", "Kamle",
        "Lohit", "Lower Dibang Valley", "Lower Subansiri",
        "Papum Pare", "Tawang", "Tirap", "West Kameng", "West Siang"
    ],
    "Assam": [
        "Baksa", "Barpeta", "Cachar", "Darrang", "Dhemaji",
        "Dhubri", "Dibrugarh", "Goalpara", "Golaghat",
        "Jorhat", "Kamrup", "Kamrup Metropolitan", "Karbi Anglong",
        "Nagaon", "Sivasagar", "Sonitpur", "Tinsukia"
    ],
    "Bihar": [
        "Araria", "Arwal", "Aurangabad", "Banka", "Begusarai",
        "Bhagalpur", "Bhojpur", "Buxar", "Darbhanga", "Gaya",
        "Gopalganj", "Jamui", "Jehanabad", "Katihar", "Madhubani",
        "Munger", "Muzaffarpur", "Nalanda", "Patna", "Purnia",
        "Rohtas", "Samastipur", "Saran", "Sitamarhi", "Siwan"
    ],
    "Chhattisgarh": [
        "Balod", "Baloda Bazar", "Bastar", "Bemetara", "Bijapur",
        "Bilaspur", "Dantewada", "Dhamtari", "Durg", "Gariaband",
        "Janjgir-Champa", "Jashpur", "Kabirdham", "Kanker",
        "Korba", "Koriya", "Mahasamund", "Raigarh", "Raipur",
        "Rajnandgaon", "Sukma", "Surajpur", "Surguja"
    ],
    "Goa": ["North Goa", "South Goa"],
    "Gujarat": [
        "Ahmedabad", "Amreli", "Anand", "Aravalli", "Banaskantha",
        "Bharuch", "Bhavnagar", "Botad", "Chhota Udaipur",
        "Dahod", "Dang", "Devbhoomi Dwarka", "Gandhinagar",
        "Gir Somnath", "Jamnagar", "Junagadh", "Kachchh",
        "Kheda", "Mahisagar", "Mehsana", "Morbi", "Narmada",
        "Navsari", "Panchmahal", "Patan", "Porbandar", "Rajkot",
        "Sabarkantha", "Surat", "Surendranagar", "Vadodara", "Valsad"
    ],
    "Haryana": [
        "Ambala", "Bhiwani", "Charkhi Dadri", "Faridabad",
        "Fatehabad", "Gurugram", "Hisar", "Jhajjar", "Jind",
        "Kaithal", "Karnal", "Kurukshetra", "Mahendragarh",
        "Nuh", "Palwal", "Panchkula", "Panipat", "Rewari",
        "Rohtak", "Sirsa", "Sonipat", "Yamunanagar"
    ],
    "Himachal Pradesh": [
        "Bilaspur", "Chamba", "Hamirpur", "Kangra", "Kinnaur",
        "Kullu", "Lahaul and Spiti", "Mandi", "Shimla",
        "Sirmaur", "Solan", "Una"
    ],
    "Jharkhand": [
        "Bokaro", "Chatra", "Deoghar", "Dhanbad", "Dumka",
        "East Singhbhum", "Garhwa", "Giridih", "Godda",
        "Gumla", "Hazaribagh", "Jamtara", "Khunti", "Koderma",
        "Latehar", "Lohardaga", "Palamu", "Ramgarh", "Ranchi",
        "Sahibganj", "Seraikela-Kharsawan", "Simdega",
        "West Singhbhum"
    ],
    "Karnataka": [
        "Bagalkot", "Ballari", "Belagavi", "Bengaluru Rural",
        "Bengaluru Urban", "Bidar", "Chamarajanagar", "Chikkaballapur",
        "Chikkamagaluru", "Chitradurga", "Dakshina Kannada",
        "Davanagere", "Dharwad", "Gadag", "Hassan", "Haveri",
        "Kalaburagi", "Kodagu", "Kolar", "Koppal", "Mandya",
        "Mysuru", "Raichur", "Ramanagara", "Shivamogga",
        "Tumakuru", "Udupi", "Uttara Kannada", "Vijayapura",
        "Yadgir"
    ],
    "Kerala": [
        "Alappuzha", "Ernakulam", "Idukki", "Kannur", "Kasaragod",
        "Kollam", "Kottayam", "Kozhikode", "Malappuram",
        "Palakkad", "Pathanamthitta", "Thiruvananthapuram",
        "Thrissur", "Wayanad"
    ],
    "Madhya Pradesh": [
        "Agar Malwa", "Alirajpur", "Anuppur", "Ashoknagar",
        "Balaghat", "Barwani", "Betul", "Bhind", "Bhopal",
        "Burhanpur", "Chhatarpur", "Chhindwara", "Damoh",
        "Datia", "Dewas", "Dhar", "Dindori", "Guna", "Gwalior",
        "Indore", "Jabalpur", "Katni", "Khandwa", "Khargone",
        "Mandla", "Mandsaur", "Morena", "Narmadapuram",
        "Neemuch", "Panna", "Raisen", "Rajgarh", "Ratlam",
        "Rewa", "Sagar", "Satna", "Sehore", "Seoni", "Shahdol",
        "Shajapur", "Sheopur", "Shivpuri", "Sidhi", "Singrauli",
        "Tikamgarh", "Ujjain", "Umaria", "Vidisha"
    ],
    "Maharashtra": [
        "Ahilyanagar", "Akola", "Amravati", "Beed", "Bhandara",
        "Buldhana", "Chandrapur", "Chhatrapati Sambhajinagar",
        "Dharashiv", "Dhule", "Gadchiroli", "Gondia",
        "Hingoli", "Jalgaon", "Jalna", "Kolhapur", "Latur",
        "Mumbai City", "Mumbai Suburban", "Nagpur", "Nanded",
        "Nandurbar", "Nashik", "Palghar", "Parbhani", "Pune",
        "Raigad", "Ratnagiri", "Sangli", "Satara", "Sindhudurg",
        "Solapur", "Thane", "Wardha", "Washim", "Yavatmal"
    ],
    "Manipur": [
        "Bishnupur", "Chandel", "Churachandpur", "Imphal East",
        "Imphal West", "Jiribam", "Kakching", "Kamjong",
        "Noney", "Pherzawl", "Senapati", "Tamenglong",
        "Tengnoupal", "Thoubal", "Ukhrul"
    ],
    "Meghalaya": [
        "East Garo Hills", "East Jaintia Hills", "East Khasi Hills",
        "Eastern West Khasi Hills", "North Garo Hills",
        "Ri-Bhoi", "South Garo Hills", "South West Garo Hills",
        "South West Khasi Hills", "West Garo Hills",
        "West Jaintia Hills", "West Khasi Hills"
    ],
    "Mizoram": [
        "Aizawl", "Champhai", "Hnahthial", "Khawzawl",
        "Kolasib", "Lawngtlai", "Lunglei", "Mamit",
        "Saiha", "Saitual", "Serchhip"
    ],
    "Nagaland": [
        "Chumoukedima", "Dimapur", "Kiphire", "Kohima",
        "Longleng", "Meluri", "Mokokchung", "Mon",
        "Niuland", "Noklak", "Peren", "Phek", "Shamator",
        "Tseminyu", "Tuensang", "Wokha", "Zunheboto"
    ],
    "Odisha": [
        "Angul", "Balangir", "Balasore", "Bargarh", "Bhadrak",
        "Boudh", "Cuttack", "Deogarh", "Dhenkanal", "Gajapati",
        "Ganjam", "Jagatsinghpur", "Jajpur", "Jharsuguda",
        "Kalahandi", "Kandhamal", "Kendrapara", "Kendujhar",
        "Khordha", "Koraput", "Malkangiri", "Mayurbhanj",
        "Nabarangpur", "Nayagarh", "Nuapada", "Puri",
        "Rayagada", "Sambalpur", "Subarnapur", "Sundargarh"
    ],
    "Punjab": [
        "Amritsar", "Barnala", "Bathinda", "Faridkot",
        "Fatehgarh Sahib", "Fazilka", "Ferozepur", "Gurdaspur",
        "Hoshiarpur", "Jalandhar", "Kapurthala", "Ludhiana",
        "Malerkotla", "Mansa", "Moga", "Pathankot", "Patiala",
        "Rupnagar", "Sahibzada Ajit Singh Nagar", "Sangrur",
        "Shaheed Bhagat Singh Nagar", "Sri Muktsar Sahib",
        "Tarn Taran"
    ],
    "Rajasthan": [
        "Ajmer", "Alwar", "Balotra", "Banswara", "Baran",
        "Barmer", "Beawar", "Bharatpur", "Bhilwara", "Bikaner",
        "Bundi", "Chittorgarh", "Churu", "Dausa", "Deeg",
        "Dholpur", "Didwana-Kuchaman", "Dungarpur", "Jaipur",
        "Jaisalmer", "Jalore", "Jhalawar", "Jhunjhunu",
        "Jodhpur", "Karauli", "Kekri", "Khairthal-Tijara",
        "Kota", "Nagaur", "Pali", "Phalodi", "Pratapgarh",
        "Rajsamand", "Sawai Madhopur", "Sikar", "Sirohi",
        "Sri Ganganagar", "Tonk", "Udaipur"
    ],
    "Sikkim": [
        "Gangtok", "Gyalshing", "Mangan", "Namchi",
        "Pakyong", "Soreng"
    ],
    "Tamil Nadu": [
        "Ariyalur", "Chengalpattu", "Chennai", "Coimbatore",
        "Cuddalore", "Dharmapuri", "Dindigul", "Erode",
        "Kallakurichi", "Kancheepuram", "Kanniyakumari",
        "Karur", "Krishnagiri", "Madurai", "Mayiladuthurai",
        "Nagapattinam", "Namakkal", "Nilgiris", "Perambalur",
        "Pudukkottai", "Ramanathapuram", "Ranipet", "Salem",
        "Sivaganga", "Tenkasi", "Thanjavur", "Theni",
        "Thoothukudi", "Tiruchirappalli", "Tirunelveli",
        "Tirupathur", "Tiruppur", "Tiruvallur",
        "Tiruvannamalai", "Tiruvarur", "Vellore",
        "Viluppuram", "Virudhunagar"
    ],
    "Telangana": [
        "Adilabad", "Bhadradri Kothagudem", "Hanumakonda",
        "Hyderabad", "Jagtial", "Jangaon", "Jayashankar Bhupalpally",
        "Jogulamba Gadwal", "Kamareddy", "Karimnagar",
        "Khammam", "Komaram Bheem Asifabad", "Mahabubabad",
        "Mahabubnagar", "Mancherial", "Medak", "Medchal-Malkajgiri",
        "Mulugu", "Nagarkurnool", "Nalgonda", "Narayanpet",
        "Nirmal", "Nizamabad", "Peddapalli", "Rajanna Sircilla",
        "Rangareddy", "Sangareddy", "Siddipet", "Suryapet",
        "Vikarabad", "Wanaparthy", "Warangal", "Yadadri Bhuvanagiri"
    ],
    "Tripura": [
        "Dhalai", "Gomati", "Khowai", "North Tripura",
        "Sepahijala", "South Tripura", "Unakoti", "West Tripura"
    ],
    "Uttar Pradesh": [
        "Agra", "Aligarh", "Ambedkar Nagar", "Amethi", "Amroha",
        "Auraiya", "Ayodhya", "Azamgarh", "Baghpat", "Bahraich",
        "Ballia", "Balrampur", "Banda", "Barabanki", "Bareilly",
        "Basti", "Bhadohi", "Bijnor", "Budaun", "Bulandshahr",
        "Chandauli", "Chitrakoot", "Deoria", "Etah", "Etawah",
        "Farrukhabad", "Fatehpur", "Firozabad", "Gautam Buddha Nagar",
        "Ghaziabad", "Ghazipur", "Gonda", "Gorakhpur", "Hamirpur",
        "Hapur", "Hardoi", "Hathras", "Jalaun", "Jaunpur",
        "Jhansi", "Kannauj", "Kanpur Dehat", "Kanpur Nagar",
        "Kasganj", "Kaushambi", "Kheri", "Kushinagar",
        "Lalitpur", "Lucknow", "Maharajganj", "Mahoba",
        "Mainpuri", "Mathura", "Mau", "Meerut", "Mirzapur",
        "Moradabad", "Muzaffarnagar", "Pilibhit", "Pratapgarh",
        "Prayagraj", "Raebareli", "Rampur", "Saharanpur",
        "Sambhal", "Sant Kabir Nagar", "Shahjahanpur",
        "Shamli", "Shravasti", "Siddharthnagar", "Sitapur",
        "Sonbhadra", "Sultanpur", "Unnao", "Varanasi"
    ],
    "Uttarakhand": [
        "Almora", "Bageshwar", "Chamoli", "Champawat",
        "Dehradun", "Haridwar", "Nainital", "Pauri Garhwal",
        "Pithoragarh", "Rudraprayag", "Tehri Garhwal",
        "Udham Singh Nagar", "Uttarkashi"
    ],
    "West Bengal": [
        "Alipurduar", "Bankura", "Birbhum", "Cooch Behar",
        "Dakshin Dinajpur", "Darjeeling", "Hooghly", "Howrah",
        "Jalpaiguri", "Jhargram", "Kalimpong", "Kolkata",
        "Malda", "Murshidabad", "Nadia", "North 24 Parganas",
        "Paschim Bardhaman", "Paschim Medinipur",
        "Purba Bardhaman", "Purba Medinipur", "Purulia",
        "South 24 Parganas", "Uttar Dinajpur"
    ],
    "Andaman and Nicobar Islands": [
        "Nicobar", "North and Middle Andaman", "South Andaman"
    ],
    "Chandigarh": ["Chandigarh"],
    "Dadra and Nagar Haveli and Daman and Diu": [
        "Dadra and Nagar Haveli", "Daman", "Diu"
    ],
    "Delhi": [
        "Central Delhi", "East Delhi", "New Delhi", "North Delhi",
        "North East Delhi", "North West Delhi", "Shahdara",
        "South Delhi", "South East Delhi", "South West Delhi",
        "West Delhi"
    ],
    "Jammu and Kashmir": [
        "Anantnag", "Bandipora", "Baramulla", "Budgam", "Doda",
        "Ganderbal", "Jammu", "Kathua", "Kishtwar", "Kulgam",
        "Kupwara", "Poonch", "Pulwama", "Rajouri", "Ramban",
        "Reasi", "Samba", "Shopian", "Srinagar", "Udhampur"
    ],
    "Ladakh": ["Kargil", "Leh"],
    "Lakshadweep": ["Lakshadweep"],
    "Puducherry": ["Karaikal", "Mahe", "Puducherry", "Yanam"]
}

# Registration function
def register():
    name = entry_name.get().strip()
    email = entry_email.get().strip()
    mobile = entry_mobile.get().strip()
    address = entry_address.get("1.0", tk.END).strip()
    pin = entry_pin.get().strip()
    password = entry_password.get()
    confirm = entry_confirm.get()
    state = state_box.get()
    district = district_box.get()

    # Check all compulsory fields
    if not all([
        name, email, mobile, address, pin,
        password, confirm, state, district
    ]):
        messagebox.showerror(
            "Error", "All fields are compulsory!"
        )
        return

    # Validate email
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        messagebox.showerror("Error", "Enter a valid email address!")
        return

    # Validate Indian mobile number
    if not re.fullmatch(r"[6-9]\d{9}", mobile):
        messagebox.showerror(
            "Error",
            "Enter a valid 10-digit Indian mobile number!"
        )
        return

    # Validate PIN code
    if not re.fullmatch(r"[1-9]\d{5}", pin):
        messagebox.showerror(
            "Error", "PIN code must be a valid 6-digit format!"
        )
        return

    # Check password
    if password != confirm:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    messagebox.showinfo(
        "Registration Successful",
        f"Welcome, {name}!\n\n"
        f"Email: {email}\n"
        f"Mobile: {mobile}\n"
        f"Address: {address}\n"
        f"State: {state}\n"
        f"District: {district}\n"
        f"PIN Code: {pin}"
    )

# Update district choices when state changes
def update_districts(event=None):
    state = state_box.get()
    district_box["values"] = states_districts.get(state, [])
    district_box.set("")

# Main window
root = tk.Tk()
root.title("Registration Form")
root.geometry("480x780")
root.resizable(False, False)

tk.Label(
    root, text="Registration Form",
    font=("Arial", 20, "bold")
).pack(pady=12)

form = tk.Frame(root)
form.pack(padx=25, fill="x")

def add_label(text, row):
    tk.Label(
        form, text=text, font=("Arial", 10)
    ).grid(row=row, column=0, sticky="w", pady=5)

def add_entry(row, show=None):
    entry = tk.Entry(form, width=32, show=show)
    entry.grid(row=row, column=1, pady=5, sticky="w")
    return entry

add_label("Full Name *", 0)
entry_name = add_entry(0)

add_label("Email *", 1)
entry_email = add_entry(1)

add_label("Mobile Number *", 2)
entry_mobile = add_entry(2)

add_label("Address *", 3)
entry_address = tk.Text(form, width=31, height=3)
entry_address.grid(row=3, column=1, pady=5)

add_label("State *", 4)
state_box = ttk.Combobox(
    form, values=sorted(states_districts.keys()),
    width=29, state="readonly"
)
state_box.grid(row=4, column=1, pady=5)
state_box.bind("<<ComboboxSelected>>", update_districts)

add_label("District *", 5)
district_box = ttk.Combobox(
    form, width=29, state="readonly"
)
district_box.grid(row=5, column=1, pady=5)

add_label("PIN Code *", 6)
entry_pin = add_entry(6)

add_label("Password *", 7)
entry_password = add_entry(7, show="*")

add_label("Confirm Password *", 8)
entry_confirm = add_entry(8, show="*")

tk.Label(
    root, text="* All fields are compulsory",
    fg="red", font=("Arial", 9)
).pack(pady=10)

tk.Button(
    root, text="Register",
    command=register,
    bg="green", fg="white",
    font=("Arial", 12, "bold"),
    width=18
).pack(pady=10)

root.mainloop()

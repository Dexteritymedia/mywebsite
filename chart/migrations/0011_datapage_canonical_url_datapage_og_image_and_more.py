# Generated by Django 4.0.2 on 2022-05-27 13:19

import core.blocks
from django.db import migrations, models
import django.db.models.deletion
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('chart', '0010_datalistingpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='datapage',
            name='canonical_url',
            field=models.URLField(blank=True, help_text="Leave blank to use the page's URL.", max_length=255, verbose_name='Canonical URL'),
        ),
        migrations.AddField(
            model_name='datapage',
            name='og_image',
            field=models.ForeignKey(blank=True, help_text='Shown when linking to this page on social media.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Preview image'),
        ),
        migrations.AddField(
            model_name='datapage',
            name='struct_org_actions',
            field=wagtail.core.fields.StreamField([('actions', wagtail.core.blocks.StructBlock([('action_type', wagtail.core.blocks.ChoiceBlock(choices=[('OrderAction', 'OrderAction'), ('ReserveAction', 'ReserveAction')], verbose_name='Action Type')), ('target', wagtail.core.blocks.URLBlock(verbose_name='Target URL')), ('language', wagtail.core.blocks.CharBlock(default='en-US', help_text='If the action is offered in multiple languages, create separate actions for each language.', verbose_name='Language')), ('result_type', wagtail.core.blocks.ChoiceBlock(choices=[('Reservation', 'Reservation'), ('BusReservation', 'BusReservation'), ('EventReservation', 'EventReservation'), ('FlightReservation', 'FlightReservation'), ('FoodEstablishmentReservation', 'FoodEstablishmentReservation'), ('LodgingReservation', 'LodgingReservation'), ('RentalCarReservation', 'RentalCarReservation'), ('ReservationPackage', 'ReservationPackage'), ('TaxiReservation', 'TaxiReservation'), ('TrainReservation', 'TrainReservation')], help_text='Leave blank for OrderAction', required=False, verbose_name='Result Type')), ('result_name', wagtail.core.blocks.CharBlock(help_text='Example: "Reserve a table", "Book an appointment", etc.', required=False, verbose_name='Result Name')), ('extra_json', wagtail.core.blocks.RawHTMLBlock(form_classname='monospace', help_text='Additional JSON-LD inserted into the Action dictionary. Must be properties of https://schema.org/Action.', required=False, verbose_name='Additional action markup'))]))], blank=True, verbose_name='Actions'),
        ),
        migrations.AddField(
            model_name='datapage',
            name='struct_org_address_country',
            field=models.CharField(blank=True, help_text='For example, USA. Two-letter ISO 3166-1 alpha-2 country code is also acceptable https://en.wikipedia.org/wiki/ISO_3166-1', max_length=255, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='datapage',
            name='struct_org_address_locality',
            field=models.CharField(blank=True, help_text='City or locality. For example, Cleveland', max_length=255, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='datapage',
            name='struct_org_address_postal',
            field=models.CharField(blank=True, help_text='Zip or postal code. For example, 44113', max_length=255, verbose_name='Postal code'),
        ),
        migrations.AddField(
            model_name='datapage',
            name='struct_org_address_region',
            field=models.CharField(blank=True, help_text='State, province, county, or region. For example, OH', max_length=255, verbose_name='State'),
        ),
        migrations.AddField(
            model_name='datapage',
            name='struct_org_address_street',
            field=models.CharField(blank=True, help_text='House number and street. For example, 55 Public Square Suite 1710', max_length=255, verbose_name='Street address'),
        ),
        migrations.AddField(
            model_name='datapage',
            name='struct_org_extra_json',
            field=models.TextField(blank=True, help_text='Additional JSON-LD inserted into the Organization dictionary. Must be properties of https://schema.org/Organization or the selected organization type.', verbose_name='Additional Organization markup'),
        ),
        migrations.AddField(
            model_name='datapage',
            name='struct_org_geo_lat',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True, verbose_name='Geographic latitude'),
        ),
        migrations.AddField(
            model_name='datapage',
            name='struct_org_geo_lng',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True, verbose_name='Geographic longitude'),
        ),
        migrations.AddField(
            model_name='datapage',
            name='struct_org_hours',
            field=wagtail.core.fields.StreamField([('hours', wagtail.core.blocks.StructBlock([('days', wagtail.core.blocks.MultipleChoiceBlock(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], help_text='For late night hours past 23:59, define each day in a separate block.', verbose_name='Days')), ('start_time', wagtail.core.blocks.TimeBlock(verbose_name='Opening time')), ('end_time', wagtail.core.blocks.TimeBlock(verbose_name='Closing time'))]))], blank=True, verbose_name='Hours of operation'),
        ),
        migrations.AddField(
            model_name='datapage',
            name='struct_org_image',
            field=models.ForeignKey(blank=True, help_text='A photo of the facility. This photo will be cropped to 1:1, 4:3, and 16:9 aspect ratios automatically.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Photo of Organization'),
        ),
        migrations.AddField(
            model_name='datapage',
            name='struct_org_logo',
            field=models.ForeignKey(blank=True, help_text='Leave blank to use the logo in Settings > Layout > Logo', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Organization logo'),
        ),
        migrations.AddField(
            model_name='datapage',
            name='struct_org_name',
            field=models.CharField(blank=True, default='', help_text='Leave blank to use the site name in Settings > Sites', max_length=255, verbose_name='Organization name'),
        ),
        migrations.AddField(
            model_name='datapage',
            name='struct_org_phone',
            field=models.CharField(blank=True, help_text='Include country code for best results. For example: +1-216-555-8000', max_length=255, verbose_name='Telephone number'),
        ),
        migrations.AddField(
            model_name='datapage',
            name='struct_org_type',
            field=models.CharField(blank=True, choices=[('Organization', 'Organization'), ('Airline', 'Organization > Airline'), ('Corporation', 'Organization > Corporation'), ('EducationalOrganization', 'Organization > EducationalOrganization'), ('CollegeOrUniversity', 'Organization > EducationalOrganization > CollegeOrUniversity'), ('ElementarySchool', 'Organization > EducationalOrganization > ElementarySchool'), ('HighSchool', 'Organization > EducationalOrganization > HighSchool'), ('MiddleSchool', 'Organization > EducationalOrganization > MiddleSchool'), ('Preschool', 'Organization > EducationalOrganization > Preschool'), ('School', 'Organization > EducationalOrganization > School'), ('GovernmentOrganization', 'Organization > GovernmentOrganization'), ('LocalBusiness', 'Organization > LocalBusiness'), ('AnimalShelter', 'Organization > LocalBusiness > AnimalShelter'), ('AutomotiveBusiness', 'Organization > LocalBusiness > AutomotiveBusiness'), ('AutoBodyShop', 'Organization > LocalBusiness > AutomotiveBusiness > AutoBodyShop'), ('AutoDealer', 'Organization > LocalBusiness > AutomotiveBusiness > AutoDealer'), ('AutoPartsStore', 'Organization > LocalBusiness > AutomotiveBusiness > AutoPartsStore'), ('AutoRental', 'Organization > LocalBusiness > AutomotiveBusiness > AutoRental'), ('AutoRepair', 'Organization > LocalBusiness > AutomotiveBusiness > AutoRepair'), ('AutoWash', 'Organization > LocalBusiness > AutomotiveBusiness > AutoWash'), ('GasStation', 'Organization > LocalBusiness > AutomotiveBusiness > GasStation'), ('MotorcycleDealer', 'Organization > LocalBusiness > AutomotiveBusiness > MotorcycleDealer'), ('MotorcycleRepair', 'Organization > LocalBusiness > AutomotiveBusiness > MotorcycleRepair'), ('ChildCare', 'Organization > LocalBusiness > ChildCare'), ('Dentist', 'Organization > LocalBusiness > Dentist'), ('DryCleaningOrLaundry', 'Organization > LocalBusiness > DryCleaningOrLaundry'), ('EmergencyService', 'Organization > LocalBusiness > EmergencyService'), ('FireStation', 'Organization > LocalBusiness > EmergencyService > FireStation'), ('Hospital', 'Organization > LocalBusiness > EmergencyService > Hospital'), ('PoliceStation', 'Organization > LocalBusiness > EmergencyService > PoliceStation'), ('EmploymentAgency', 'Organization > LocalBusiness > EmploymentAgency'), ('EntertainmentBusiness', 'Organization > LocalBusiness > EntertainmentBusiness'), ('AdultEntertainment', 'Organization > LocalBusiness > EntertainmentBusiness > AdultEntertainment'), ('AmusementPark', 'Organization > LocalBusiness > EntertainmentBusiness > AmusementPark'), ('ArtGallery', 'Organization > LocalBusiness > EntertainmentBusiness > ArtGallery'), ('Casino', 'Organization > LocalBusiness > EntertainmentBusiness > Casino'), ('ComedyClub', 'Organization > LocalBusiness > EntertainmentBusiness > ComedyClub'), ('MovieTheater', 'Organization > LocalBusiness > EntertainmentBusiness > MovieTheater'), ('NightClub', 'Organization > LocalBusiness > EntertainmentBusiness > NightClub'), ('FinancialService', 'Organization > LocalBusiness > FinancialService'), ('AccountingService', 'Organization > LocalBusiness > FinancialService > AccountingService'), ('AutomatedTeller', 'Organization > LocalBusiness > FinancialService > AutomatedTeller'), ('BankOrCreditUnion', 'Organization > LocalBusiness > FinancialService > BankOrCreditUnion'), ('InsuranceAgency', 'Organization > LocalBusiness > FinancialService > InsuranceAgency'), ('FoodEstablishment', 'Organization > LocalBusiness > FoodEstablishment'), ('Bakery', 'Organization > LocalBusiness > FoodEstablishment > Bakery'), ('BarOrPub', 'Organization > LocalBusiness > FoodEstablishment > BarOrPub'), ('Brewery', 'Organization > LocalBusiness > FoodEstablishment > Brewery'), ('CafeOrCoffeeShop', 'Organization > LocalBusiness > FoodEstablishment > CafeOrCoffeeShop'), ('FastFoodRestaurant', 'Organization > LocalBusiness > FoodEstablishment > FastFoodRestaurant'), ('IceCreamShop', 'Organization > LocalBusiness > FoodEstablishment > IceCreamShop'), ('Restaurant', 'Organization > LocalBusiness > FoodEstablishment > Restaurant'), ('Winery', 'Organization > LocalBusiness > FoodEstablishment > Winery'), ('GovernmentOffice', 'Organization > LocalBusiness > GovernmentOffice'), ('PostOffice', 'Organization > LocalBusiness > GovernmentOffice > PostOffice'), ('HealthAndBeautyBusiness', 'Organization > LocalBusiness > HealthAndBeautyBusiness'), ('BeautySalon', 'Organization > LocalBusiness > HealthAndBeautyBusiness > BeautySalon'), ('DaySpa', 'Organization > LocalBusiness > HealthAndBeautyBusiness > DaySpa'), ('HairSalon', 'Organization > LocalBusiness > HealthAndBeautyBusiness > HairSalon'), ('HealthClub', 'Organization > LocalBusiness > HealthAndBeautyBusiness > HealthClub'), ('NailSalon', 'Organization > LocalBusiness > HealthAndBeautyBusiness > NailSalon'), ('TattooParlor', 'Organization > LocalBusiness > HealthAndBeautyBusiness > TattooParlor'), ('HomeAndConstructionBusiness', 'Organization > LocalBusiness > HomeAndConstructionBusiness'), ('Electrician', 'Organization > LocalBusiness > HomeAndConstructionBusiness > Electrician'), ('GeneralContractor', 'Organization > LocalBusiness > HomeAndConstructionBusiness > GeneralContractor'), ('HVACBusiness', 'Organization > LocalBusiness > HomeAndConstructionBusiness > HVACBusiness'), ('HousePainter', 'Organization > LocalBusiness > HomeAndConstructionBusiness > HousePainter'), ('Locksmith', 'Organization > LocalBusiness > HomeAndConstructionBusiness > Locksmith'), ('MovingCompany', 'Organization > LocalBusiness > HomeAndConstructionBusiness > MovingCompany'), ('Plumber', 'Organization > LocalBusiness > HomeAndConstructionBusiness > Plumber'), ('RoofingContractor', 'Organization > LocalBusiness > HomeAndConstructionBusiness > RoofingContractor'), ('InternetCafe', 'Organization > LocalBusiness > InternetCafe'), ('LegalService', 'Organization > LocalBusiness > LegalService'), ('Attorney', 'Organization > LocalBusiness > LegalService > Attorney'), ('Notary', 'Organization > LocalBusiness > LegalService > Notary'), ('Library', 'Organization > LocalBusiness > Library'), ('LodgingBusiness', 'Organization > LocalBusiness > LodgingBusiness'), ('BedAndBreakfast', 'Organization > LocalBusiness > LodgingBusiness > BedAndBreakfast'), ('Campground', 'Organization > LocalBusiness > LodgingBusiness > Campground'), ('Hostel', 'Organization > LocalBusiness > LodgingBusiness > Hostel'), ('Hotel', 'Organization > LocalBusiness > LodgingBusiness > Hotel'), ('Motel', 'Organization > LocalBusiness > LodgingBusiness > Motel'), ('Resort', 'Organization > LocalBusiness > LodgingBusiness > Resort'), ('ProfessionalService', 'Organization > LocalBusiness > ProfessionalService'), ('RadioStation', 'Organization > LocalBusiness > RadioStation'), ('RealEstateAgent', 'Organization > LocalBusiness > RealEstateAgent'), ('RecyclingCenter', 'Organization > LocalBusiness > RecyclingCenter'), ('SelfStorage', 'Organization > LocalBusiness > SelfStorage'), ('ShoppingCenter', 'Organization > LocalBusiness > ShoppingCenter'), ('SportsActivityLocation', 'Organization > LocalBusiness > SportsActivityLocation'), ('BowlingAlley', 'Organization > LocalBusiness > SportsActivityLocation > BowlingAlley'), ('ExerciseGym', 'Organization > LocalBusiness > SportsActivityLocation > ExerciseGym'), ('GolfCourse', 'Organization > LocalBusiness > SportsActivityLocation > GolfCourse'), ('HealthClub', 'Organization > LocalBusiness > SportsActivityLocation > HealthClub'), ('PublicSwimmingPool', 'Organization > LocalBusiness > SportsActivityLocation > PublicSwimmingPool'), ('SkiResort', 'Organization > LocalBusiness > SportsActivityLocation > SkiResort'), ('SportsClub', 'Organization > LocalBusiness > SportsActivityLocation > SportsClub'), ('StadiumOrArena', 'Organization > LocalBusiness > SportsActivityLocation > StadiumOrArena'), ('TennisComplex', 'Organization > LocalBusiness > SportsActivityLocation > TennisComplex'), ('Store', 'Organization > LocalBusiness > Store'), ('AutoPartsStore', 'Organization > LocalBusiness > Store > AutoPartsStore'), ('BikeStore', 'Organization > LocalBusiness > Store > BikeStore'), ('BookStore', 'Organization > LocalBusiness > Store > BookStore'), ('ClothingStore', 'Organization > LocalBusiness > Store > ClothingStore'), ('ComputerStore', 'Organization > LocalBusiness > Store > ComputerStore'), ('ConvenienceStore', 'Organization > LocalBusiness > Store > ConvenienceStore'), ('DepartmentStore', 'Organization > LocalBusiness > Store > DepartmentStore'), ('ElectronicsStore', 'Organization > LocalBusiness > Store > ElectronicsStore'), ('Florist', 'Organization > LocalBusiness > Store > Florist'), ('FurnitureStore', 'Organization > LocalBusiness > Store > FurnitureStore'), ('GardenStore', 'Organization > LocalBusiness > Store > GardenStore'), ('GroceryStore', 'Organization > LocalBusiness > Store > GroceryStore'), ('HardwareStore', 'Organization > LocalBusiness > Store > HardwareStore'), ('HobbyShop', 'Organization > LocalBusiness > Store > HobbyShop'), ('HomeGoodsStore', 'Organization > LocalBusiness > Store > HomeGoodsStore'), ('JewelryStore', 'Organization > LocalBusiness > Store > JewelryStore'), ('LiquorStore', 'Organization > LocalBusiness > Store > LiquorStore'), ('MensClothingStore', 'Organization > LocalBusiness > Store > MensClothingStore'), ('MobilePhoneStore', 'Organization > LocalBusiness > Store > MobilePhoneStore'), ('MovieRentalStore', 'Organization > LocalBusiness > Store > MovieRentalStore'), ('MusicStore', 'Organization > LocalBusiness > Store > MusicStore'), ('OfficeEquipmentStore', 'Organization > LocalBusiness > Store > OfficeEquipmentStore'), ('OutletStore', 'Organization > LocalBusiness > Store > OutletStore'), ('PawnShop', 'Organization > LocalBusiness > Store > PawnShop'), ('PetStore', 'Organization > LocalBusiness > Store > PetStore'), ('ShoeStore', 'Organization > LocalBusiness > Store > ShoeStore'), ('SportingGoodsStore', 'Organization > LocalBusiness > Store > SportingGoodsStore'), ('TireShop', 'Organization > LocalBusiness > Store > TireShop'), ('ToyStore', 'Organization > LocalBusiness > Store > ToyStore'), ('WholesaleStore', 'Organization > LocalBusiness > Store > WholesaleStore'), ('TelevisionStation', 'Organization > LocalBusiness > TelevisionStation'), ('TouristInformationCenter', 'Organization > LocalBusiness > TouristInformationCenter'), ('TravelAgency', 'Organization > LocalBusiness > TravelAgency'), ('MedicalOrganization', 'Organization > MedicalOrganization'), ('Dentist', 'Organization > MedicalOrganization > Dentist'), ('Hospital', 'Organization > MedicalOrganization > Hospital'), ('Pharmacy', 'Organization > MedicalOrganization > Pharmacy'), ('Physician', 'Organization > MedicalOrganization > Physician'), ('NGO', 'Organization > NGO'), ('PerformingGroup', 'Organization > PerformingGroup'), ('DanceGroup', 'Organization > PerformingGroup > DanceGroup'), ('MusicGroup', 'Organization > PerformingGroup > MusicGroup'), ('TheaterGroup', 'Organization > PerformingGroup > TheaterGroup'), ('SportsOrganization', 'Organization > SportsOrganization'), ('SportsTeam', 'Organization > SportsOrganization > SportsTeam')], default='', help_text='If blank, no structured data will be used on this page.', max_length=255, verbose_name='Organization type'),
        ),
        migrations.AlterField(
            model_name='datapage',
            name='content',
            field=wagtail.core.fields.StreamField([('full_richtext', core.blocks.RichtextBlock()), ('simple_richtext', core.blocks.SimpleRichtextBlock()), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('shadow', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Add Shadow'), ('S', 'Small Shadow'), ('R', 'Regular Shadow'), ('L', 'Larger Shadow')], required=False))])), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='blocks/table_block.html'))], blank=True, null=True),
        ),
    ]

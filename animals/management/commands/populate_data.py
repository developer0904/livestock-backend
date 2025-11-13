from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime, timedelta
import random

from animals.models import Animal
from owners.models import Owner
from events.models import Event
from inventory.models import InventoryItem


class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating sample data...')
        
        # Clear existing data
        Animal.objects.all().delete()
        Owner.objects.all().delete()
        Event.objects.all().delete()
        InventoryItem.objects.all().delete()
        
        # Create Owners
        owners_data = [
            {
                'first_name': 'John', 'last_name': 'Smith',
                'email': 'john.smith@example.com', 'phone': '555-0101',
                'address': '123 Farm Road', 'city': 'Springfield', 'state': 'Illinois',
                'zip_code': '62701', 'farm_name': 'Smith Family Farm', 'farm_size': 150.5
            },
            {
                'first_name': 'Mary', 'last_name': 'Johnson',
                'email': 'mary.johnson@example.com', 'phone': '555-0102',
                'address': '456 Ranch Drive', 'city': 'Austin', 'state': 'Texas',
                'zip_code': '73301', 'farm_name': 'Johnson Ranch', 'farm_size': 250.0
            },
            {
                'first_name': 'Robert', 'last_name': 'Williams',
                'email': 'robert.williams@example.com', 'phone': '555-0103',
                'address': '789 Country Lane', 'city': 'Madison', 'state': 'Wisconsin',
                'zip_code': '53701', 'farm_name': 'Williams Dairy Farm', 'farm_size': 200.25
            },
        ]
        
        owners = []
        for data in owners_data:
            owner = Owner.objects.create(**data)
            owners.append(owner)
            self.stdout.write(f'Created owner: {owner.full_name}')
        
        # Create Animals
        species_breeds = {
            'cattle': ['Holstein', 'Angus', 'Hereford', 'Jersey'],
            'sheep': ['Merino', 'Suffolk', 'Dorset'],
            'goat': ['Boer', 'Nubian', 'Alpine'],
            'pig': ['Yorkshire', 'Duroc', 'Hampshire'],
        }
        
        animals = []
        for i in range(30):
            species = random.choice(list(species_breeds.keys()))
            breed = random.choice(species_breeds[species])
            gender = random.choice(['male', 'female'])
            
            animal = Animal.objects.create(
                tag_id=f'A{1000 + i}',
                name=f'{breed} {i+1}' if random.random() > 0.5 else None,
                species=species,
                breed=breed,
                gender=gender,
                date_of_birth=(datetime.now().date() - timedelta(days=random.randint(30, 1825))),
                color=random.choice(['Brown', 'Black', 'White', 'Mixed']),
                weight=random.uniform(50, 800),
                owner=random.choice(owners),
                acquisition_date=(datetime.now().date() - timedelta(days=random.randint(1, 730))),
                acquisition_price=random.uniform(500, 3000),
                status=random.choice(['healthy', 'healthy', 'healthy', 'sick', 'pregnant']),
            )
            animals.append(animal)
            
        self.stdout.write(f'Created {len(animals)} animals')
        
        # Create Events
        event_types = ['vaccination', 'treatment', 'checkup', 'breeding', 'birth']
        for i in range(50):
            Event.objects.create(
                event_type=random.choice(event_types),
                animal=random.choice(animals),
                date=(datetime.now().date() - timedelta(days=random.randint(0, 365))),
                title=f'Event {i+1}',
                description=f'Description for event {i+1}',
                cost=random.uniform(0, 500),
                veterinarian='Dr. Smith' if random.random() > 0.5 else None,
            )
        
        self.stdout.write('Created 50 events')
        
        # Create Inventory Items
        inventory_data = [
            {'name': 'Hay Bales', 'category': 'feed', 'quantity': 500, 'unit': 'unit', 
             'reorder_level': 100, 'unit_price': 8.50},
            {'name': 'Cattle Feed Mix', 'category': 'feed', 'quantity': 2000, 'unit': 'kg',
             'reorder_level': 500, 'unit_price': 2.25},
            {'name': 'Penicillin', 'category': 'medicine', 'quantity': 50, 'unit': 'bottle',
             'reorder_level': 10, 'unit_price': 15.99},
            {'name': 'Vitamins Supplement', 'category': 'supplement', 'quantity': 100, 'unit': 'bottle',
             'reorder_level': 20, 'unit_price': 12.50},
            {'name': 'Syringes', 'category': 'equipment', 'quantity': 200, 'unit': 'unit',
             'reorder_level': 50, 'unit_price': 1.50},
        ]
        
        for data in inventory_data:
            InventoryItem.objects.create(**data)
        
        self.stdout.write('Created inventory items')
        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))

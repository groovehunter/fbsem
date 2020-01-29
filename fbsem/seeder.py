from django_seed import Seed

seeder = Seed.seeder()

from relations.models import Person, PeopleGroup
seeder.add_entity(Person, 5)
seeder.add_entity(PeopleGroup, 10)

inserted_pks = seeder.execute()

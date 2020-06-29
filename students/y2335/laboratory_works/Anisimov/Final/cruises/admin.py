from django.contrib import admin
from cruises.models import MotorshipTeam, Motorship, Sailor, Cruis, Tour, Route, CruisRoute, TicketCategory, Ticket

# Register your models here.

admin.site.register(MotorshipTeam)
admin.site.register(Motorship)
admin.site.register(Sailor)
admin.site.register(Cruis)
admin.site.register(Tour)
admin.site.register(Route)
admin.site.register(CruisRoute)
admin.site.register(TicketCategory)
admin.site.register(Ticket)
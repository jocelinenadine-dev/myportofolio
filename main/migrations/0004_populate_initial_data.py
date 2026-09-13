from django.db import migrations
import uuid
import datetime

import sys

def populate_data(apps, schema_editor):
    if 'test' in sys.argv:
        return
    Experience = apps.get_model('main', 'Experience')
    Award = apps.get_model('main', 'Award')

    if Experience.objects.count() == 0:
        experiences = [
            {
                "id": uuid.UUID("c2e3c80c-0a77-4314-b6e2-c7ffd46a0f28"),
                "title": "BEM FASILKOM UI — Sports Department",
                "description": "Department Staff & Supporter Treasurer — Managing Badminton club operations, athlete appreciation events, and financial budgeting for Laskar Biru Merah.",
                "category": "organization",
                "ended_at": None,
            },
            {
                "id": uuid.UUID("6d483027-1a6f-4f8a-ad49-2bad577bd42b"),
                "title": "COMPFEST 18 — FASILKOM UI",
                "description": "Event Staff (Playground Main Event) — Coordinating operations for Indonesia's largest student-led technology festival, managing exhibitor and divisional workflows.",
                "category": "committee",
                "ended_at": None,
            },
            {
                "id": uuid.UUID("e35d1cbf-d24c-41e6-a594-705bb5c7c971"),
                "title": "Ikatan Koko Cici Jakarta (KOCI)",
                "description": "DKI Jakarta Provincial Board (Graphic Design) — Serving on the provincial executive board to lead creative branding, visual assets, tourism promotion, and cultural diplomacy.",
                "category": "organization",
                "ended_at": None,
            },
            {
                "id": uuid.UUID("ba1af3f9-cf36-4871-bee6-3654783243a1"),
                "title": "Forum Generasi Berencana (GenRe)",
                "description": "BKKBN Central Jakarta (Human Resources) — Talent management, onboarding, and training sessions for youth ambassadors advocating adolescent health and family planning across Central Jakarta.",
                "category": "organization",
                "ended_at": None,
            },
            {
                "id": uuid.UUID("1f8c5f1c-4294-490c-8155-0faa8b703238"),
                "title": "Google Student Ambassador (GSA)",
                "description": "Selected among top 2,000+ ambassadors nationwide from 81,000+ applicants; championed Google technologies, AI adoption, and digital literacy initiatives within campus.",
                "category": "ambassador",
                "ended_at": datetime.datetime(2025, 6, 1, tzinfo=datetime.timezone.utc),
            },
            {
                "id": uuid.UUID("973de705-c126-41ef-a830-bda3dced921b"),
                "title": "SISTECH FASILKOM UI",
                "description": "Front-End Engineering Intern — Completed front-end development training, UI engineering workshops, and an industrial visit to Grab Indonesia.",
                "category": "committee",
                "ended_at": datetime.datetime(2026, 6, 1, tzinfo=datetime.timezone.utc),
            },
            {
                "id": uuid.UUID("e3b3a1cb-6c60-4326-b133-90e44ca0a896"),
                "title": "Open House FASILKOM UI 2026",
                "description": "Documentation & Engagement Crew (DEC) — Directed creative multimedia content and managed promotional campaigns introducing computer science programs to prospective students.",
                "category": "committee",
                "ended_at": datetime.datetime(2026, 6, 1, tzinfo=datetime.timezone.utc),
            },
            {
                "id": uuid.UUID("eb13d594-7ec0-44f0-a2f3-63afd2ef4d6f"),
                "title": "Majelis Perwakilan Kelas (MPK) SMAK 2 PENABUR",
                "description": "President / Chairperson — Led the student legislative council overseeing 10+ OSIS programs, established schoolwide standardized ID policy, and achieved the Gold Standardization Award.",
                "category": "organization",
                "ended_at": datetime.datetime(2024, 6, 1, tzinfo=datetime.timezone.utc),
            },
            {
                "id": uuid.UUID("24466ff7-21d8-4ee6-9fae-a45fdbff8f1f"),
                "title": "REXAR MINARA — Annual School Cup",
                "description": "Head of Fundraising & Finance — Spearheaded an entrepreneurial fundraising strategy that successfully doubled event revenue compared to the prior year, marking the school's most successful cup.",
                "category": "committee",
                "ended_at": datetime.datetime(2025, 6, 1, tzinfo=datetime.timezone.utc),
            },
            {
                "id": uuid.UUID("f19c147f-3a04-4211-9631-117b961c4840"),
                "title": "Tim Pendidik Sebaya (Peer Educators)",
                "description": "President / Team Lead — Certified in peer counseling, organized adolescent health campaigns, and fostered an inclusive school environment for student welfare.",
                "category": "organization",
                "ended_at": datetime.datetime(2024, 6, 1, tzinfo=datetime.timezone.utc),
            },
            {
                "id": uuid.UUID("78765572-218d-47a5-a28e-0820ff8171c0"),
                "title": "REXAR NUMINOUS & MARE NOSTRA",
                "description": "Publication & Competition Staff — Managed public relations and event operations for national inter-school competitions, including MonsoonSIM business simulation tournaments.",
                "category": "committee",
                "ended_at": datetime.datetime(2024, 6, 1, tzinfo=datetime.timezone.utc),
            },
        ]
        for item in experiences:
            Experience.objects.create(**item)

    if Award.objects.count() == 0:
        awards = [
            {
                "id": uuid.UUID("c5cea4b7-670f-487b-9beb-eed02cff611d"),
                "title": "Puteri Duta Generasi Berencana (GenRe) Kota Jakarta Pusat",
                "issuer": "BKKBN Kota Jakarta Pusat",
                "category": "advocacy",
                "rank": "1st Winner & Best Group Talent",
                "year": "2024",
                "description": "Selected as 1st Winner and Best Group Talent after 3 audition stages and 3-week quarantine; served as youth ambassador advocating adolescent health, mental wellness, and life planning.",
            },
            {
                "id": uuid.UUID("ff72124b-1101-4199-835e-81c933cbacf9"),
                "title": "Puteri Duta GenRe Provinsi DKI Jakarta",
                "issuer": "BKKBN Provinsi DKI Jakarta",
                "category": "advocacy",
                "rank": "Favorite Winner",
                "year": "2024",
                "description": "Represented Central Jakarta at the provincial level following 1-month quarantine, speech defense on GenRe substance pillars, and provincial talent showcase.",
            },
            {
                "id": uuid.UUID("0eeeec09-41bc-4574-8944-7922843f7032"),
                "title": "Koko Cici Jakarta 2026",
                "issuer": "Ikatan Koko Cici Jakarta & Dinas Pariwisata dan Ekonomi Kreatif DKI Jakarta",
                "category": "pageant",
                "rank": "Finalist & Cultural Ambassador",
                "year": "2026",
                "description": "Selected as Finalist for official Chinese-Indonesian cultural and tourism ambassadorship in DKI Jakarta, completing intensive quarantine, talent exhibitions, and cultural diplomacy programs.",
            },
            {
                "id": uuid.UUID("71ae15bf-b64b-4317-804a-aa59e5b28441"),
                "title": "Business Model Canvas (BMC) Competition",
                "issuer": "SMAK 2 PENABUR Jakarta · Inter-School Business Competition",
                "category": "business",
                "rank": "1st Place Winner",
                "year": "2022",
                "description": "Led a student team to design and defend a 9-block Business Model Canvas for an innovative sustainable extract enterprise within a 24-hour competition sprint.",
            },
            {
                "id": uuid.UUID("69dbf007-cdaf-460f-aecd-d315e833300a"),
                "title": "National TB Educational Video Competition",
                "issuer": "Puskesmas Sawah Besar · World TB Day",
                "category": "public-health",
                "rank": "2nd Place Winner",
                "year": "2024",
                "description": "Conducted 5W+1H public health research, wrote the educational screenplay, and directed video production in 2 days to raise community awareness on tuberculosis prevention.",
            },
        ]
        for item in awards:
            Award.objects.create(**item)


def rollback_data(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_experience_category'),
    ]

    operations = [
        migrations.RunPython(populate_data, rollback_data),
    ]

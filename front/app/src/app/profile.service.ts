import { Injectable } from '@angular/core';
import { Tutor } from './models/Tutor';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProfileService {

  dummyTutor : Tutor = {
    tutorId: 0,
    firstName: 'John',
    lastName: 'Smith',
    courses: [
      {
        classPrefix: 'MATH',
        classNumber: 3163
      },
      {
        classPrefix: 'CS',
        classNumber: 4485
      },
      {
        classPrefix: 'CS',
        classNumber: 3377
      }
    ],
    appointments: [
      {
        appointmentId: 0,
        studentId: 1,
        tutorId: 0,
        tutorName: 'John Smith',
        studentName: 'Jane Doe',
        time: 'Wed Oct 25 2023.11:00 AM',
        subject: 'CS 3377'
      },
      {
        appointmentId: 1,
        studentId: 1,
        tutorId: 0,
        tutorName: 'John Smith',
        studentName: 'Jane Doe',
        time: 'Tue Oct 24 2023.10:30 AM'
      },
      {
        appointmentId: 2,
        studentId: 1,
        tutorId: 0,
        tutorName: 'John Smith',
        studentName: 'Jane Doe',
        time: 'Sat Oct 28 2023.11:00 AM',
        subject: 'MATH 3163'
      }
    ],
    tutorSchedule: [
      "Tue Oct 24 2023.10:30 AM",
      "Tue Oct 24 2023.11:00 AM",
      "Tue Oct 24 2023.11:30 AM",
      "Tue Oct 24 2023.12:00 PM",
      "Wed Oct 25 2023.10:30 AM",
      "Wed Oct 25 2023.11:00 AM",
      "Wed Oct 25 2023.11:30 AM",
      "Wed Oct 25 2023.12:00 PM",
      "Fri Oct 27 2023.10:30 AM",
      "Fri Oct 27 2023.11:00 AM",
      "Fri Oct 27 2023.11:30 AM",
      "Fri Oct 27 2023.12:00 PM",
      "Sat Oct 28 2023.10:30 AM",
      "Sat Oct 28 2023.11:00 AM",
      "Sat Oct 28 2023.11:30 AM",
      "Sat Oct 28 2023.12:00 PM",
      "Mon Oct 30 2023.10:30 AM",
      "Mon Oct 30 2023.11:00 AM",
      "Mon Oct 30 2023.11:30 AM",
      "Mon Oct 30 2023.12:00 PM",
    ]
  }

  constructor() { }

  getTutorProfile(id : number) : Observable<Tutor>
  {
    return of(this.dummyTutor); //TODO: get from http
  }
}

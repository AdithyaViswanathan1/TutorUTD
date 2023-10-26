export interface Appointment
{
    appointmentId: number;
    tutorId: number;
    studentId: number;
    tutorName: string;
    studentName: string;
    time: string;
    subject?: string;
}
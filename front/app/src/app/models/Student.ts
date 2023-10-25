import { Appointment } from "./Appointment";

export interface Student
{
    studentId: number;
    firstName: string;
    lastName: string;
    appointments?: Appointment[];
}
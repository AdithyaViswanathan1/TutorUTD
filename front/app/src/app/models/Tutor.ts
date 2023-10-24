import { Appointment } from "./Appointment";
import { Course } from "./Course";

export interface Tutor
{
    tutorId: number;
    firstName: string;
    lastName: string;
    profilePicture?: File;
    courses: Course[];
    appointments?: Appointment[];
    tutorSchedule?: string[];
}
import { Appointment } from "./Appointment";

export interface Tutor
{
    tutorId: number;
    fullName: string;
    aboutMe?: string;
    totalHours: number;
    available: boolean;
    profilePicture?: File;
    courses: string[];
    appointments?: Appointment[];
    tutorSchedule?: string[];
}
import { Appointment } from "./Appointment";

export interface Tutor
{
    tutor_id: number;
    full_name: string;
    total_hours: number;
    available: boolean;
    profile_picture?: string;
    subjects: string[];
    times?: string[];
    background_checked?: boolean;
    biography: string;
}
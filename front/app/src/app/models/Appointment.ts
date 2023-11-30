export interface Appointment
{
    id: number;
    tutor_id: number;
    student_id: number;
    tutor_name: string;
    student_name: string;
    time: string;
    course?: string;
    completed: boolean;
}
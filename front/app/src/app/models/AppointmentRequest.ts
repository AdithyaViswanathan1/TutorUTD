export interface AppointmentRequest {
    dates: string[];
    student_id: number;
    tutor_id: number;
    location?: string;
    course?: string;
}
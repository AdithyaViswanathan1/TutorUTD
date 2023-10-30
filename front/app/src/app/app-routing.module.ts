import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LandingPageComponent } from './landing-page/landing-page.component';
import { LoginComponent } from './login/login.component';
import { SignUpComponent } from './sign-up/sign-up.component';
import { ProfileComponent } from './profile/profile.component';
import { AppointmentsComponent } from './appointments/appointments.component';
import { SearchComponent } from './search/search.component';

const routes: Routes = [
  {path: '', component: LandingPageComponent},
  {path: 'login/:userType', component: LoginComponent},
  {path: 'signup/:userType', component: SignUpComponent},
  {path: 'profile/:tutorId', component: ProfileComponent},
  {path: 'appointments/:userType/:id', component: AppointmentsComponent},
  {path: 'search', component: SearchComponent},
  {path: 'search/:tutorName', component: SearchComponent},
  {path: 'search/:tutorName/:subject', component: SearchComponent},
  {path: 'search/:tutorName/:subject/:classNum', component: SearchComponent},
  {path: 'search/:subject', component: SearchComponent},
  {path: 'search/:subject/:classNum', component: SearchComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

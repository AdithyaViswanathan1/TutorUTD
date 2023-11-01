import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LandingPageComponent } from './landing-page/landing-page.component';

import { NavbarComponent } from './navbar/navbar.component';
import { SignUpComponent } from './sign-up/sign-up.component';
import { LoginComponent } from './login/login.component';
import { SearchComponent } from './search/search.component';
import { AppointmentsComponent } from './appointments/appointments.component';
import { ProfileComponent } from './profile/profile.component';
import { TimeTableComponent } from './time-table/time-table.component';
import { CancelConfirmationComponent } from './modals/cancel-confirmation/cancel-confirmation.component';
import { BookSessionComponent } from './modals/book-session/book-session.component';
import { BookingConfirmationComponent } from './modals/booking-confirmation/booking-confirmation.component';
import { DeselectWarningComponent } from './modals/deselect-warning/deselect-warning.component';
import { CookieService } from 'ngx-cookie-service';

@NgModule({
  declarations: [
    AppComponent,
    LandingPageComponent,
    NavbarComponent,
    SignUpComponent,
    LoginComponent,
    SearchComponent,
    AppointmentsComponent,
    ProfileComponent,
    TimeTableComponent,
    CancelConfirmationComponent,
    BookSessionComponent,
    BookingConfirmationComponent,
    DeselectWarningComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FontAwesomeModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [
    CookieService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
